import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')


def ask(prompt):
    if not openai.api_key:
        raise EnvironmentError('Chave da API da OpenAI nao configurada')
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': prompt}]
    )
    return response['choices'][0]['message']['content']
