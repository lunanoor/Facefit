from flask import Flask, request, jsonify, send_from_directory
from analysis_engine import FaceAnalyzer
from recommendations import get_recommendations
import os

app = Flask(__name__, static_folder='static', static_url_path='')
analyzer = FaceAnalyzer()

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    file = request.files['image']
    image_bytes = file.read()
    
    try:
        analysis_result = analyzer.analyze_image(image_bytes)
        
        if not analysis_result:
             return jsonify({"error": "No face detected in the image."}), 400

        recommendations = get_recommendations(analysis_result['face_shape'], analysis_result['skin_tone'])
        
        response = {
            "analysis": analysis_result,
            "recommendations": recommendations
        }
        
        return jsonify(response)

    except Exception as e:
        print(f"Error processing image: {e}")
        return jsonify({"error": "Internal server error processing image."}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
