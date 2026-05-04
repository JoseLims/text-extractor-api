from datetime import datetime, timedelta
from app.extensions import db


class Session(db.Model):
    __tablename__ = "sessions"

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(255), nullable=False, unique=True)
    client_id = db.Column(db.Integer, db.ForeignKey("clients.id"), nullable=False)
    expires_at = db.Column(db.DateTime, nullable=False)

    client = db.relationship("Client")

    def __init__(self, token: str, client_id: int, duration_minutes=60):
        self.token = token
        self.client_id = client_id
        self.expires_at = datetime.utcnow() + timedelta(minutes=duration_minutes)