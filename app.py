import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

VISION_ENDPOINT = os.getenv("https://asdaasdasdads.cognitiveservices.azure.com/")
VISION_KEY = os.getenv("74zfy9oNEFghoq9YhWvdkz4P73G2fC9t3tfMqgqndVvwUhu7TX1MJQQJ99BJAC5T7U2XJ3w3AAAFACOGLsqX")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "image" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["image"]
        if file.filename == "":
            return jsonify({"error": "Empty filename"}), 400

        # Call Azure Vision API
        analyze_url = f"{VISION_ENDPOINT}/vision/v3.2/analyze"
        headers = {
            "Ocp-Apim-Subscription-Key": VISION_KEY,
            "Content-Type": "application/octet-stream"
        }
        params = {"visualFeatures": "Categories,Description,Objects,Tags"}
        response = requests.post(
            analyze_url,
            headers=headers,
            params=params,
            data=file.read()
        )

        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": response.text}), response.status_code

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)

