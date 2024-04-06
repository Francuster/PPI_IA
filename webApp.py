from flask import Flask, request, jsonify
from chatbot import generate_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    text = request.args.get('input')
    if text is None:
        return jsonify({"error": "No input provided"}), 400

    resultado = generate_response(text)
    return jsonify({"request": text, "response": resultado})