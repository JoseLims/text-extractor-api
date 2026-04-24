from app.extensions import db


class Client(db.Model):
    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)

    documents = db.relationship("Document", backref="client", lazy=True)

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email