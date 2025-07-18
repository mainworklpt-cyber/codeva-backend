from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = "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"
MODEL = "deepseek/deepseek-r1-0528-qwen3-8b:free"

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get('message')

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "তুমি একজন স্মার্ট হ্যাকার ভাইয়ের বাংলা AI অ্যাসিস্ট্যান্ট। সংক্ষেপে, কনফিডেন্ট, ইমোজি সহ বাংলা উত্তর দেবে।"},
            {"role": "user", "content": user_msg}
        ]
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost"
    }

    try:
        res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        reply = res.json()['choices'][0]['message']['content']
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": "❌ CODEVA: সমস্যা হইছে ভাই!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
