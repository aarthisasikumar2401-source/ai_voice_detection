from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/detect", methods=["POST"])
def detect():
    data = request.get_json()
    if not data or "audio_base64" not in data:
        return jsonify({"error": "audio_base64 field is required"})
    
    return jsonify({
        "classification": "HUMAN",
        "confidence_score": 0.92,
        "explanation": "Placeholder detection logic for Round 1",
        "supported_languages": ["Tamil", "English", "Hindi", "Malayalam", "Telugu"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
