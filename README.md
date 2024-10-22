## Setup Project Locally


1. Clone project

    ```
    git clone https://github.com/ankitsmt211/task_manager.git
    ```

1. Setup virtual environment
    ```
   python -m venv venv # create virtual enviroment
   source venv/bin/active # active virtual environment
   ```
   
1. Install Dependencies
    ```
   pip install -r requirements.txt
   ```
   
1. Migrations

   ```
   python manage.py migrate
   ```
   
1. Run local Server
    ```
   python manage.py runserver
   ```
   
---

## APIs
1. CREATE TASK
   ```
    POST <local_base_url>/api/v1/task/
   ```

    Payload:
    ```
    {
    "name": "task 5",
    "description": "description task 5",
    "task_type":"unknown"
   }
    ```
   
   Response:
   ```
   {
    "id": "c33eb150-64ff-498a-b061-6e36cd996d64",
    "name": "task 5",
    "description": "description task 5",
    "task_type": "unknown",
    "completed_at": null,
    "status": "TODO",
    "users": []
   }
   ```
   
1. ASSIGN TASK TO USER

   ```
   POST <local_base_url>/api/v1/user/<user_id>/task/<task_id>/assign/
   ```
   
   Payload: None

   Response:
   ```
   "Task assigned to user"
   ```

1. GET ALL TASKS FOR USER

   ```
   GET <local_base_url>/api/v1/user/<user_id>/task/list/?page=1
   ```
   
   Response:
   ```
   {
    "items": [
        {
            "id": "182e93e0-c580-49e9-b2c6-c2596710a55d",
            "name": "task 2",
            "description": null,
            "created_at": "2024-10-22T05:25:03.327057Z",
            "task_type": null,
            "completed_at": null,
            "status": "TODO",
            "users": [
                "ad17ef1f-d5bc-4292-89b5-3b57a674f616",
                "bb83a08b-bef7-409b-96bc-de8efa30d0a1"
            ]
        }
    ],
    "count": 1,
    "page_size": 10,
    "page": 1
   }
   ```
   

---
## Sample Data Script

To generate sample user data, follow these steps:

1. Open the Python interactive shell:
   ```bash
   python manage.py shell

1. Copy complete file from this path
    ```
   users/scripts/sample_user_data.py
   ```
   
1. Paste into python shell and hit enter to run

NOTE: You can use API to create tasks

---
## Django ADMIN

1. create superuser 

   ```
   python manage.py createsuperuser 
   ```
   
2. Login to admin using super user credentials
   
   ```
   <local_base_url>/admin
   ```