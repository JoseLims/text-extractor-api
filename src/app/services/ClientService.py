from app.extensions import db
from app.models.Client import Client
from datetime import datetime


class ClientService:

    @staticmethod
    def create(data):
        name = data.get("name")
        email = data.get("email")

        if not name or not email:
            raise ValueError("Nome e email são obrigatórios.")

        existing = Client.query.filter_by(email=email).first()
        if existing:
            raise ValueError("Email já cadastrado.")

        client = Client(
            name=name,
            email=email
        )

        db.session.add(client)
        db.session.commit()

        return client

    @staticmethod
    def find_by_id(client_id: int):
        client = Client.query.filter_by(id=client_id, deleted_at=None).first()

        if not client:
            raise LookupError("Cliente não encontrado.")

        return client

    @staticmethod
    def list(page=1, limit=10, name=None):
        query = Client.query.filter_by(deleted_at=None)

        if name:
            query = query.filter(Client.name.ilike(f"%{name}%"))

        pagination = query.paginate(page=page, per_page=limit, error_out=False)

        return pagination

    @staticmethod
    def update(client_id: int, data):
        client = Client.query.filter_by(id=client_id, deleted_at=None).first()

        if not client:
            raise LookupError("Cliente não encontrado.")

        name = data.get("name")
        email = data.get("email")

        if name:
            client.name = name

        if email:
            client.email = email

        db.session.commit()

        return client

    @staticmethod
    def delete(client_id: int):
        client = Client.query.filter_by(id=client_id, deleted_at=None).first()

        if not client:
            raise LookupError("Cliente não encontrado.")

        client.deleted_at = datetime.utcnow()
        db.session.commit()

        return True