from dataclasses import dataclass
import requests


@dataclass
class RequestsClient:
    base_url: str
    api_key: str
    access_token: str
    client: requests.Session

    def __init__(self, base_url: str, access_token=""):
        self.base_url = base_url
        self.access_token = access_token
        self.client = requests.Session()

        self.client.headers = {
            "Authorization": "Token token=" + self.access_token,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def get(self, uri: str, query_params: dict) -> requests.Response:
        return self.client.get(self.base_url + uri, params=query_params)
