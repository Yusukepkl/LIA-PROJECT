import os
from grook import Grook

GROOK_API_KEY = os.getenv('GROOK_API_KEY')

class GrookClient:
    def __init__(self):
        self.client = Grook(GROOK_API_KEY)

    def analyze(self, text: str) -> dict:
        return self.client.analyze(text)
