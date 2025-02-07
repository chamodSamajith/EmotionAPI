from flask import Flask, request, jsonify
#from flask_cors import CORS
from deepface import DeepFace


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! Flask API is running 2."

@app.route('/analyze-emotion', methods=['POST'])
def analyze_emotion():
    try:
        print("API hit! update ")
        # Get the image file from the request
        image_file = request.files['image']
        if not image_file:
            return jsonify({"error": "No image file provided"}), 400

        # Save the image to a temporary file
        image_path = "temp_image.jpg"
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

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))  # Use Azure-assigned port
    app.run(debug=True, host="0.0.0.0", port=port)
