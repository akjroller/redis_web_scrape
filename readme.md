# Redis-Based Data Processing Scripts

This repository contains a set of Python scripts utilizing Redis for data processing. The scripts perform various tasks, such as adding initial data to Redis sets, scraping URLs, and processing email tasks.

## Scripts

### 1. add_initial_data.py

- Adds an initial email and URL to respective Redis sets.
- Usage:
  ```bash
 python add_initial_data.py

### 2. url_processing.py
 - Continuously processes URLs and emails from Redis sets, adding them to corresponding queues. 
 - Usage:
  ```bash
 python add_initial_data.py
 ```
### 3. web_scraping.py
- Scrapes content from URLs, extracts new URLs and email addresses, and adds them to Redis sets.
- Usage:
```bash
  python web_scraping.py
```
### 4. add_urls_to_csv.py
- Periodically processes URLs from a Redis queue and updates a CSV file.
- Usage:
```bash
python add_urls_to_csv.py
```

### 5. process_email_tasks.py
- Processes email tasks from a Redis queue and updates a CSV file.
- Usage:
```bash
 python process_email_tasks.py
```

# Configuration

Modify the scripts with your actual Redis server information, queue names, file names, and intervals based on your requirements.

## Prerequisites

- Python (Version 3.x)
- Redis server running locally or with proper connection details
- Install requirements using requirements.txt
```bash
pip install -r requierment.txt
```