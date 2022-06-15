# Manually migrate tasks from one Google account to another using Google Tasks API

from Google import Create_Service, convert_to_RFC_datetime
from dotenv import load_dotenv() # Environmental variables
import json

load_dotenv()

CLIENT_SECRET_FILE = 'client_secret_file.json' # Get this from GCP
API_NAME = 'tasks'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/tasks'] # Read & write access

# Redirects to login page; sign in with desired Google account
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
print(dir(service))

# Get default lists
response = service.tasklists().list().execute()
listItems = response.get('items')
print(listItems)

# From above information copy the desired task list ID
taskListID = os.getenv('TASK_LIST_ID')

# File with tasks to insert
with open('request_tasks.json') as file:
    tasks = json.loads(file.read())

print(tasks[0])

def construct_request_body(task):
    try:
        request_body = task
        return request_body
    except Exception:
        return None

# Insert to list
for i in range(len(tasks)):
    service.tasks().insert(
        tasklist=taskListID,
        body=construct_request_body(tasks[i]),
    ).execute()

print("END")