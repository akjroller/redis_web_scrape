import redis

def add_initial_email(redis_host, redis_port, redis_password):
    try:
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password)
        email_set = 'emails_found'
        initial_email = 'akjroller@gmail.com'

        if not r.sismember(email_set, initial_email):
            r.sadd(email_set, initial_email)
            print(f"Initial email '{initial_email}' added to the Redis set.")
    except Exception as e:
        print(f"Error adding initial email to Redis: {e}")

def add_initial_url(redis_host, redis_port, redis_password):
    try:
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        discovered_urls_set = 'discovered_urls'
        initial_url = 'https://thehackernews.com/'

        if not r.sismember(discovered_urls_set, initial_url):
            r.sadd(discovered_urls_set, initial_url)
            print(f"Initial URL '{initial_url}' added to the Redis set.")
    except Exception as e:
        print(f"Error adding initial URL to Redis: {e}")

if __name__ == "__main__":
    redis_host = "localhost"
    redis_port = 6379
    redis_password = ""

    add_initial_email(redis_host, redis_port, redis_password)
    add_initial_url(redis_host, redis_port, redis_password)
