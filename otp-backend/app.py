from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///otp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class OTP(db.Model):
    id = db.Column(db.String, primary_key=True)
    value = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def serialize(self):
        return {
            "id": self.id,
            "value": self.value,
            "created_at": self.created_at.isoformat()
        }

with app.app_context():
    db.create_all()

@app.route('/otp', methods=['POST'])
def create_otp():
    data = request.json
    otp = OTP(id=data['id'], value=data['value'])
    db.session.add(otp)
    db.session.commit()
    return jsonify({"status": "created"}), 201

@app.route('/otp/<otp_id>', methods=['GET'])
def read_otp(otp_id):
    otp = OTP.query.get(otp_id)
    if not otp:
        return jsonify({"error": "OTP not found"}), 404
    result = otp.serialize()
    db.session.delete(otp)  # delete after read
    db.session.commit()
    return jsonify(result)

@app.route('/otp', methods=['GET'])
def list_otps():
    otps = OTP.query.all()
    return jsonify([otp.serialize() for otp in otps])

if __name__ == "__main__":
    app.run(debug=True)