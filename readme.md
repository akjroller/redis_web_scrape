# Redis-Based Data Processing Scripts

This repository contains a set of Python scripts utilizing Redis for data processing. The scripts perform various tasks, such as adding initial data to Redis sets, scraping URLs, and processing email tasks.

## Scripts

### 1. first_task.py

- Adds an initial email and URL to respective Redis sets.
- Don't forget to add the first email and urls in
- Usage:
```bash
 python first_task.py
```

### 2. create_tasks.py
 - Continuously processes URLs and emails from Redis sets, adding them to corresponding queues. 
 - Usage:
  ```bash
 python create_tasks.py
 ```
### 3. execute_scraping_tasks.py
- Scrapes content from URLs, extracts new URLs and email addresses, and adds them to Redis sets.
- Usage:
```bash
  python execute_scraping_tasks.py
```
### 4. execute_add_to_list_tasks.py
- Periodically processes URLs from a Redis queue and updates a CSV file.
- Usage:
```bash
python execute_add_to_list_tasks.py
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