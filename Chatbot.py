#pip install openai

import openai 

API = "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"
openai.api_key = API
completion =openai.Completion()

def Answer(question):
    prompt = f'You : {question}\nAssistant : '
    response = completion.create(
        model = "gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature = 0.5,
        max_tokens = 60,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0)
    ans = response.choices[0].text.strip()
    return ans

while True:
     n=input("Query : ")
     print(Answer(n))"
openai.api_key = API
completion =openai.Completion()

def Answer(question):
    prompt = f'You : {question}\nAssistant : '
    response = completion.create(
        model = "gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature = 0.5,
        max_tokens = 60,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0)
    ans = response.choices[0].text.strip()
    return ans

while True:
     n=input("Query : ")
     print(Answer(n))
