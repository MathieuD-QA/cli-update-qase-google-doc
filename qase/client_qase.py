import requests
from dotenv import load_dotenv
import os


class Qase:
    def __init__(self):
        self.url_default = "https://api.github.com/user"
        self.payload = ""
        self.api_key = load_dotenv()

    def internall_call(self, boolean_post):
        if boolean_post:
            requests.post(f"{self.url_default}")
        else:
            requests.get(f"{self.url_default}")

    def get_test_run_id(self, type_request):
        self.internall_call(type_request)


a = Qase()

print(a.get_test_run_id(False))

