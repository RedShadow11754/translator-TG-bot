import json
import httpx
import requests
import os
import dotenv
dotenv.load_dotenv()
key = os.getenv('API_KEY')
url = "https://api.translateapi.ai/api/v1/translate/"


class TranslatorBot:
    def __init__(self, data):
        self.url = "https://api.translateapi.ai/api/v1/translate/"
        self.key = os.getenv('API_KEY')
        self.headers = {
    "Authorization": f"Bearer {self.key}",
    "Content-Type": "application/json"
}
        self.data = data
    async def translate(self):
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.post(
                self.url,
                headers=self.headers,
                json=self.data
            )
            result = response.json()
            return result["translated_text"]