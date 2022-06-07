import requests
from dotenv import load_dotenv
import os


class Qase:
    def __init__(self):
        self.payload = ""
        self.api_key = load_dotenv()


    def internall_call(self, boolean_post,url):
        headers = {
            "Accept": "application/json",
            "Token": os.getenv("QASE_API_KEY")
        }


        if boolean_post:
            response = requests.post(f"https://api.qase.io/v1/{url}", headers=headers)
            print(response.text)
        else:
            response = requests.get(f"https://api.qase.io/v1/{url}",  headers=headers)
            json_res = response.json()
            google_drive_payload = {
                "id": json_res["result"]["id"],
                "title": json_res["result"]["title"],
                "description": json_res["result"]["description"],
                "status_text": json_res["result"]["status_text"],
                "total":  json_res["result"]["stats"]["total"],
                "passed": json_res["result"]["stats"]["passed"],
                "blocked": json_res["result"]["stats"]["blocked"],
                "in_progress":json_res["result"]["stats"]["in_progress"]
            }
            print(google_drive_payload)







    def get_test_run_id(self):
        self.internall_call(False,"run/ECOM/722")



