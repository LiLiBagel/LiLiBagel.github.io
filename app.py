from flask import Flask, request, jsonify
from flask_cors import CORS
from ChatGPT import get_ai_response

app = Flask(__name__)
CORS(app)  # 啟用CORS，允許來自任何來源的請求

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data['input'].encode("utf-8").decode("latin1")
    response = get_ai_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
