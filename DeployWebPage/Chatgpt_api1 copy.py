import openai
from openai import OpenAI

client = OpenAI()
openai.api_key = 'sk-proj-7Gnk6rkfcFu8hCOcbKDGT3BlbkFJex8YtEfJYWAqevBMAADq'

def get_ai_response(prompt):
    
    response = client.completions.create(
        model="ft:davinci-002:personal::9foev6P4",#gpt-3.5-turbo-instruct
        prompt = prompt,
        max_tokens=200,
    )   
    return response.choices[0].text

