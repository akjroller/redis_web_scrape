import redis
import csv
import time


def connect_to_redis(redis_host, redis_port, redis_password):
    try:
        return redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
    except Exception as e:
        print(f"Error connecting to Redis: {e}")
        return None


def get_url_from_queue(redis_client, queue_name):
    _, url = redis_client.blpop(queue_name)
    return url


def update_csv_file(csv_filename, url):
    try:
        with open(csv_filename, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([url])
            print(f"Added {url} to the CSV file.")
    except Exception as e:
        print(f"Error updating CSV file: {e}")


def add_urls_to_csv(redis_client, add_to_list_queue, csv_filename):
    url = get_url_from_queue(redis_client, add_to_list_queue)

    if url:
        update_csv_file(csv_filename, url)
    else:
        print("No new URLs found in the Redis queue.")


def main(redis_host, redis_port, redis_password, add_to_list_queue, csv_filename, interval):
    redis_client = connect_to_redis(redis_host, redis_port, redis_password)

    if redis_client is None:
        return

    while True:
        add_urls_to_csv(redis_client, add_to_list_queue, csv_filename)
        time.sleep(interval)


if __name__ == "__main__":
    redis_host = "localhost"
    redis_port = 6379
    redis_password = ""

    add_to_list_queue = 'add_to_list_queue'

    csv_filename = 'urls.csv'

    interval = 10

    main(redis_host, redis_port, redis_password, add_to_list_queue, csv_filename, interval)
