from flask import Flask, request, jsonify
from chatbot import generate_response
from loginHuella import decode_and_verify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chatbot', methods=['GET'])
def chatbot_request():
    text = request.args.get('input')
    if text is None:
        return jsonify({"error": "No input provided"}), 400

    resultado = generate_response(text)
    return jsonify({"request": text, "response": resultado})


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part in the request'}), 400

    image_file = request.files['image']

    # If the user does not select a file, the browser submits an empty file without a filename
    if image_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400


    user = decode_and_verify(image_file)

    response = {}

    if user:
        response = {
            'authenticated': True,
            'user': user
        }
    else:
        response = {
            'authenticated': False,
            'user': 'none'
        }

    return jsonify(response), 200;