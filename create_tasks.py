import redis
import time

def connect_to_redis(redis_host, redis_port, redis_password):
    try:
        return redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
    except Exception as e:
        print(f"Error connecting to Redis: {e}")
        return None

def process_url(url, redis_client):
    redis_client.rpush("scraping_queue", url)
    print(f"Added {url} task to queue")

    redis_client.rpush("add_to_list_queue", url)
    print(f"Added {url} to CSV task queue")

def process_email(email, redis_client):
    redis_client.rpush("email_addresses_tasks", email)
    print(f"Added {email} task to emails_found queue")

def process_urls(redis_client):
    try:
        while True:
            url = redis_client.spop("discovered_urls")
            email = redis_client.spop("emails_found_set")

            if url is not None:
                process_url(url, redis_client)

            if email is not None:
                process_email(email, redis_client)

            if url is None and email is None:
                time.sleep(10)

    except Exception as e:
        print(f"Error processing URLs: {e}")

def main(redis_host, redis_port, redis_password):
    redis_client = connect_to_redis(redis_host, redis_port, redis_password)

    if redis_client is not None:
        process_urls(redis_client)

if __name__ == "__main__":
    redis_host = "localhost"
    redis_port = 6379
    redis_password = ""

    main(redis_host, redis_port, redis_password)
