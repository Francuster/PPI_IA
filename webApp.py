from flask import Flask, request, jsonify
from chatbot import generate_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    text = request.args.get('input')
    if text is None:
        return jsonify({"error": "No input provided"}), 400

    resultado = generate_response(text)
    return jsonify({"request": text, "response": resultado})