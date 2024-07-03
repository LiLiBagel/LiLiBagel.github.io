from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import openai
import os
from openai import OpenAI

client = OpenAI()
app = Flask(__name__)
CORS(app)  # 啟用CORS，允許來自任何來源的請求

# 使用從環境變量中獲取的OpenAI API密鑰
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def serve_frontend():
    return send_from_directory('.', 'test.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data['input'].encode("utf-8").decode("latin1")
    
    # 使用 ChatGPT API 獲取回應
    response = client.completions.create(
        model="ft:davinci-002:personal::9foev6P4",#gpt-3.5-turbo-instruct
        prompt = user_input,
        max_tokens=200,
    )   
    return response.choices[0].text


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
