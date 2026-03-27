import os


class Config:
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{os.getenv('DB_USER', 'extractions')}:"
        f"{os.getenv('DB_PASSWORD', 'extractions')}@"
        f"{os.getenv('DB_HOST', 'db')}:"
        f"{os.getenv('DB_PORT', '5432')}/"
        f"{os.getenv('DB_NAME', 'extractions')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False