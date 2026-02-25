import flask
import requests
import json
from collections import OrderedDict
from flask import Flask, request, jsonify, url_for, redirect
import os

# ===================================================================
UPLOAD_FOLDER = "backend/files"
# ===================================================================

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)

@app.route('/')
def main():
    return "Hello testing", 200


@app.route('/gotostt', methods=['POST'])
def take_audio():

    if "file" not in request.files:
        return jsonify({"error":"No file provided"}), 400
    
    file = request.files['file']

    if file.filename == "":
        return jsonify({"error":"Empty filename"}), 400
    
    save_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(save_path)

    return jsonify({"message":"File received",
                    "filename":file.filename
                    }), 200




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3500, debug=True)