from flask import Flask, jsonify, request
import random

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Backend is running"})

@app.route("/detect", methods=["POST"])
def detect_voice():
    data = request.get_json()

    if not data or "audio_base64" not in data:
        return jsonify({"error": "audio_base64 field is required"}), 400

    classification = random.choice(["AI_GENERATED", "HUMAN"])
    confidence = round(random.uniform(0.7, 0.99), 2)

    return jsonify({
        "classification": classification,
        "confidence_score": confidence,
        "explanation": "Placeholder detection logic for Round 1",
        "supported_languages": ["Tamil", "English", "Hindi", "Malayalam", "Telugu"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0",)
