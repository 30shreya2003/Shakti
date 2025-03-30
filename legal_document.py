
from flask import Blueprint, request, jsonify
import torch
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer


legal_bp = Blueprint('legal', __name__)


IPC_DETAILS = {
    "384": {
        "title": "Extortion",
        "definition": "Whoever intentionally puts any person in fear of any injury to that person or any other, and thereby dishonestly induces the person so put in fear to deliver to any person any property or valuable security.",
        "punishment": "Imprisonment up to 3 years, or fine, or both.",
        "remedies": [
            "Immediate FIR registration",
            "Preservation of threat evidence",
            "Protection order from magistrate"
        ]
    },
    "354": {
        "title": "Assault or Criminal Force to Woman with Intent to Outrage her Modesty",
        "definition": "Whoever assaults or uses criminal force to any woman, intending to outrage or knowing it to be likely that he will thereby outrage her modesty.",
        "punishment": "Imprisonment up to 2 years, or fine, or both.",
        "remedies": [
            "Medical examination",
            "Statement recording by woman officer",
            "Protection order"
        ]
    },
    "354A": {
        "title": "Sexual Harassment",
        "definition": "Unwelcome physical contact and advances or demand or request for sexual favors or showing pornography against the will of a woman or making sexually colored remarks.",
        "punishment": "Up to 3 years imprisonment, or fine, or both.",
        "remedies": [
            "Complaint to Internal Committee",
            "Preserve digital evidence",
            "Right to transfer perpetrator"
        ]
    },
    "354D": {
        "title": "Stalking",
        "definition": "Following a woman or contacting or attempting to contact her despite clear indication of disinterest by her.",
        "punishment": "Up to 3 years imprisonment (first offense), up to 5 years (repeat offense).",
        "remedies": [
            "Restraining order",
            "Preserve call/SMS logs",
            "Cyber cell complaint"
        ]
    },
    "506": {
        "title": "Criminal Intimidation",
        "definition": "Whoever threatens another with injury to person, reputation or property with intent to cause alarm.",
        "punishment": "Up to 2 years imprisonment, or fine, or both.",
        "remedies": [
            "Preserve threat evidence",
            "Protection order",
            "Weapon seizure if applicable"
        ]
    },
    "509": {
        "title": "Word, Gesture or Act Intended to Insult Modesty",
        "definition": "Whoever intentionally uses words, sounds or gestures to intrude upon the privacy of a woman.",
        "punishment": "Simple imprisonment up to 1 year, or fine, or both.",
        "remedies": [
            "Audio/video evidence preservation",
            "Witness statements",
            "Community protection order"
        ]
    }
}

@legal_bp.route('/generate', methods=['POST'])  
def generate_document():
    try:
        data = request.get_json()  
        
        
        text = data.get('complaint_text', '').strip()
        if not text:
            return jsonify({"error": "Complaint text is required"}), 400
        
        
        ipc_section = "354" if "assault" in text.lower() else "506"
        
        return jsonify({
            "ipc_section": ipc_section,
            "details": IPC_DETAILS.get(ipc_section, {})
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500