from flask import Flask, request, jsonify
from flask_cors import CORS
from deepface import DeepFace
import os
import uuid

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for front-end compatibility

# Pre-load the DeepFace model at startup
DeepFace.build_model('Emotion')

@app.route('/analyze-emotion', methods=['POST'])
def analyze_emotion():
    try:
        # Get the image file from the request
        image_file = request.files['image']
        if not image_file:
            return jsonify({"error": "No image file provided"}), 400

        # Create a unique temporary file name
        image_path = f"temp_image_{uuid.uuid4().hex}.jpg"
        image_file.save(image_path)

        # Analyze the uploaded image
        analysis = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=False)

        # Handle batch mode (list output) and single-image mode (dictionary output)
        if isinstance(analysis, list):
            analysis = analysis[0]  # Get the first analysis from the list

        # Extract the dominant emotion and detailed probabilities
        result = {
            "dominant_emotion": analysis.get('dominant_emotion', "Unknown"),
            "emotions": analysis.get('emotion', {})
        }

        # Remove the temporary file
        os.remove(image_path)

        return jsonify(result), 200

    except ValueError as ve:
        return jsonify({"error": f"Value error: {str(ve)}"}), 400
    except FileNotFoundError as fe:
        return jsonify({"error": f"File error: {str(fe)}"}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
