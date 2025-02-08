# import io
# from PIL import Image
from flask import Flask , jsonify
# , request
# from transformers import pipeline

app = Flask(__name__)

# Load the emotion classification pipeline
# emotion_classifier = pipeline("image-classification", model="dima806/facial_emotions_image_detection")

# @app.route('/classify_emotion', methods=['POST'])
# def classify_emotion():
#     # Check if the request contains an image
#     if 'image' not in request.files:
#         return jsonify({'error': 'No image provided'}), 400

#     image_file = request.files['image']
    
#     # Read and process the image
#     image_bytes = image_file.read()
#     image = Image.open(io.BytesIO(image_bytes))

#     # Perform emotion classification
#     results = emotion_classifier(image)

#     # Extract the top prediction
#     top_prediction = results[0]
#     emotion = top_prediction['label']
#     confidence = top_prediction['score']

#     # Prepare the response
#     response = {
#         'emotion': emotion,
#         'confidence': confidence
#     }

#     return jsonify(response)

@app.route('/')
def home():
    return "Hello, World! Flask API."

# @app.route('/health', methods=['GET'])
# def health_check():
#     return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)



# pillow
# transformers
# torch