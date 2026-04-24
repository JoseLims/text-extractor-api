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

    @staticmethod
    def update(client_id: int, name: str, email: str) -> Client:
        client = Client.query.get(client_id)

        if not client:
            raise LookupError("Cliente não encontrado.")

        if not name or not name.strip():
            raise ValueError("O nome do cliente é obrigatório.")

        if not email or not email.strip():
            raise ValueError("O email do cliente é obrigatório.")

        existing_client = Client.query.filter_by(email=email.strip()).first()
        if existing_client and existing_client.id != client.id:
            raise ValueError("Já existe um cliente com esse email.")

        try:
            client.name = name.strip()
            client.email = email.strip()

            db.session.commit()
            return client

        except Exception as error:
            db.session.rollback()
            raise ValueError(f"Erro ao atualizar o cliente: {error}")