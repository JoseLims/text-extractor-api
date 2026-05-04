"""add password hash, sessions table, and deleted_at columns

Revision ID: 0f4d3a1b5c2e
Revises: a95319fb954e
Create Date: 2026-04-30 00:00:00.000000
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f4d3a1b5c2e'
down_revision = 'a95319fb954e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('clients', sa.Column('password_hash', sa.String(length=255), nullable=False, server_default=''))
    op.add_column('clients', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    op.add_column('documents', sa.Column('deleted_at', sa.DateTime(), nullable=True))

    op.create_table(
        'sessions',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('token', sa.String(length=255), nullable=False),
        sa.Column('client_id', sa.Integer(), nullable=False),
        sa.Column('expires_at', sa.DateTime(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
        sa.UniqueConstraint('token')
    )


def downgrade():
    op.drop_table('sessions')
    op.drop_column('documents', 'deleted_at')
    op.drop_column('clients', 'deleted_at')
    op.drop_column('clients', 'password_hash')
