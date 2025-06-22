from googleapiclient.discovery import build
import os

API_KEY = os.getenv('GOOGLE_API_KEY')
CX = os.getenv('GOOGLE_CX')


def search(query, num=5):
    if not API_KEY or not CX:
        raise EnvironmentError('Chaves da API do Google nao configuradas')
    service = build('customsearch', 'v1', developerKey=API_KEY)
    res = service.cse().list(q=query, cx=CX, num=num).execute()
    return res.get('items', [])
