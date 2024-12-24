import os
from dotenv import load_dotenv


load_dotenv()

class Headers:

    basic_auth = {
        "Authorization": f"Bearer {os.environ["API_TOKEN"]}",
        "X-Task-Id": "API-1"
    }
