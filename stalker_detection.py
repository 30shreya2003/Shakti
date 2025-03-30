from flask import Blueprint, request, jsonify

stalker_blueprint = Blueprint('stalker', __name__)

@stalker_blueprint.route('/predict', methods=['POST'])
def predict_stalker():
    try:
        data = request.get_json()
        print("📩 Received JSON:", data)  

        if not data:
            return jsonify({"error": "Invalid request, JSON required"}), 400

        latitude = float(data.get('latitude', 0))
        longitude = float(data.get('longitude', 0))
        time_diff = float(data.get('time_diff', 0))
        distance_diff = float(data.get('distance_diff', 0))

        if time_diff > 20 and distance_diff > 150:
            result = "⚠️ Stalker Detected!"
        else:
            result = "✅ No suspicious activity detected."

        print("✅ Detection Result:", result)  
        return jsonify({'result': result})

    except Exception as e:
        print("❌ Error:", str(e)) 
        return jsonify({'error': str(e)}), 400
