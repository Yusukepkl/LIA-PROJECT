import os
from googleapiclient.discovery import build

CSE_ID = os.getenv('GOOGLE_CSE_ID')
API_KEY = os.getenv('GOOGLE_API_KEY')

class GoogleSearch:
    def __init__(self):
        self.service = build("customsearch", "v1", developerKey=API_KEY)

    def search(self, query: str):
        res = self.service.cse().list(q=query, cx=CSE_ID).execute()
        return [item['link'] for item in res.get('items', [])]
