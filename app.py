# from flask import Flask, request, jsonify
# from flask_cors import CORS  # Import CORS

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         data = request.get_json()

#         latitude = float(data['latitude'])
#         longitude = float(data['longitude'])
#         time_diff = float(data['time_diff'])
#         distance_diff = float(data['distance_diff'])

#         # Your ML model logic (example)
#         if time_diff > 20 and distance_diff > 150:
#             result = "⚠️ Stalker Detected!"
#         else:
#             result = "✅ No suspicious activity detected."

#         return jsonify({'result': result})
    
#     except Exception as e:
#         return jsonify({'error': str(e)}), 400  # Return error if any issue occurs

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask
# from flask_cors import CORS
# from stalker_detection import stalker_blueprint
# from legal_document import legal_doc_blueprint

# app = Flask(__name__)
# CORS(app)

# # Register Blueprints
# app.register_blueprint(stalker_blueprint, url_prefix='/stalker')
# app.register_blueprint(legal_doc_blueprint)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask
from flask_cors import CORS
from stalker_detection import stalker_blueprint
from legal_document import legal_bp
from repeat_offenders import repeat

app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(stalker_blueprint, url_prefix='/stalker')
app.register_blueprint(legal_bp, url_prefix='/legal')
app.register_blueprint(repeat, url_prefix="/repeat")
if __name__ == '__main__':
    app.run(debug=True)