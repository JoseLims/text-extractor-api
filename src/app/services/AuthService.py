import uuid
from datetime import datetime, timedelta

from app.extensions import db
from app.models.Client import Client
from app.models.Session import Session


class AuthService:
    SESSION_DURATION = 60  # minutos

    @staticmethod
    def login(email: str, password: str):
        if not email or not password:
            raise ValueError("Email e senha são obrigatórios.")

        client = Client.query.filter_by(email=email).first()

        if not client:
            raise LookupError("Credenciais inválidas.")

        token = str(uuid.uuid4())

        session = Session(
            token=token,
            client_id=client.id,
            duration_minutes=AuthService.SESSION_DURATION
        )

        db.session.add(session)
        db.session.commit()

        return session

    @staticmethod
    def validate_session(token: str):
        if not token:
            raise LookupError("Token não informado.")

        session = Session.query.filter_by(token=token).first()

        if not session:
            raise LookupError("Sessão inválida.")

        if session.expires_at < datetime.utcnow():
            raise LookupError("Sessão expirada.")

        session.expires_at = datetime.utcnow() + timedelta(minutes=AuthService.SESSION_DURATION)
        db.session.commit()

        return session