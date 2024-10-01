import aiohttp


class RequestsClient:
    base_url: str
    api_key: str

    def __init__(self, base_url: str, access_token=""):
        self.base_url = base_url
        self.access_token = access_token

    async def get(self, uri: str, query_params: dict) -> aiohttp.ClientResponse:
        headers = {
            "Authorization": "Token token=" + self.access_token,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        client = aiohttp.ClientSession(headers=headers)
        return await client.get(self.base_url + uri, params=query_params)
