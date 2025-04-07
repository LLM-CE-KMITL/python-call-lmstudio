import requests

def ask_llm(prompt):
    url = 'http://localhost:1234/v1/chat/completions'
    headers = {'Content-Type': 'application/json; charset=utf-8'}

    data = {
        'messages': [
            {
                'role': 'system',
                'content': 'You are a useful assistant'
            },
            {
                'role': 'user',
                'content': prompt
            }
        ],
        'model':'llama-3.2-3b-instruct',
        'max_tokens': -1, 
        'temperature': 0.7, 
        'top_k': 10, 
        'repetition_penalty': 1.05, 
        'stream': False
    }

    response = requests.post(url, headers=headers, json=data)

    return response.json()['choices'][0]['message']['content']


ask_llm('What is the Capital City of Thailand?')
