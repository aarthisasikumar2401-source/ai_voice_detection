from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Backend is running"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "audio_base64" not in data:
        return jsonify({"error": "audio_base64 missing"}), 400

    
    result = {
        "classification": "HUMAN",
        "confidence": 0.85,
        "language": "English"
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
