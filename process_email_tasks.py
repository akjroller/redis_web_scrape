import redis
import csv
import time


def process_email_tasks(redis_client, csv_filename):
    try:
        email = redis_client.blpop('email_addresses_tasks')

        if email:
            email = email[1]
            with open(csv_filename, 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([email])
                csvfile.flush()
                print(f"Added {email} to the CSV file.")
        else:
            print("No new email addresses found in the Redis queue.")

    except Exception as e:
        print(f"Error adding email addresses to CSV: {e}")


if __name__ == "__main__":
    redis_host = "localhost"
    redis_port = 6379
    redis_password = ""

    redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
    csv_filename = 'email_addresses.csv'

    while True:
        process_email_tasks(redis_client, csv_filename)
        time.sleep(1)
