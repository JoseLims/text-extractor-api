from app.extensions import db
from app.models.Client import Client


class ClientService:
    @staticmethod
    def create(name: str, email: str) -> Client:
        if not name or not name.strip():
            raise ValueError("O nome do cliente é obrigatório.")

        if not email or not email.strip():
            raise ValueError("O email do cliente é obrigatório.")

        existing_client = Client.query.filter_by(email=email).first()
        if existing_client:
            raise ValueError("Já existe um cliente com esse email.")

        client = Client(
            name=name.strip(),
            email=email.strip()
        )

        db.session.add(client)
        db.session.commit()

        return client

    @staticmethod
    def find_by_id(client_id: int) -> Client:
        client = Client.query.get(client_id)

        if not client:
            raise LookupError("Cliente não encontrado.")

        return client