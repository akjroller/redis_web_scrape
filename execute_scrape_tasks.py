import redis
import requests
from bs4 import BeautifulSoup
import re

def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        return None

def extract_urls_and_emails(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    new_urls = [link.get('href') for link in soup.find_all('a', href=True)]
    email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', html_content)

    return new_urls, email_addresses

def add_urls_to_redis(redis_client, discovered_urls_set, urls):
    unique_urls = [url for url in urls if not redis_client.sismember(discovered_urls_set, url) and url.startswith('http')]
    if unique_urls:
        redis_client.sadd(discovered_urls_set, *unique_urls)
        print(f"Added {len(unique_urls)} new unique URLs to the set.")

def add_emails_to_redis(redis_client, emails_found_set, email_addresses):
    unique_email_addresses = list(set(email_addresses))
    if unique_email_addresses:
        redis_client.sadd(emails_found_set, *unique_email_addresses)
        print(f"Found and added unique email addresses: {', '.join(unique_email_addresses)} to 'emails_found' set")

def scrape_url(url, redis_client, discovered_urls_set, emails_found_set):
    html_content = get_html_content(url)

    if html_content is not None:
        soup = BeautifulSoup(html_content, 'html.parser')
        title_tag = soup.title

        if title_tag:
            title = title_tag.text.strip()
            print(f"Scraped '{title}' from {url}")

            new_urls, email_addresses = extract_urls_and_emails(html_content)

            add_urls_to_redis(redis_client, discovered_urls_set, new_urls)
            add_emails_to_redis(redis_client, emails_found_set, email_addresses)
        else:
            print(f"Title not found for {url}")
    else:
        print(f"HTML content is empty for {url}")


def main():
    redis_host = "localhost"
    redis_port = 6379
    redis_password = ""

    redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

    queue_name = 'scraping_queue'
    discovered_urls_set = 'discovered_urls'
    emails_found_set = 'emails_found'

    while True:
        _, url = redis_client.blpop(queue_name)
        if url:
            scrape_url(url, redis_client, discovered_urls_set, emails_found_set)
        else:
            print("No new URLs found in the Redis queue.")

if __name__ == "__main__":
    main()
