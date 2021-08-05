"""create users

Revision ID: 651e05d2cc2e
Revises: 
Create Date: 2021-08-05 13:00:56.617266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '651e05d2cc2e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(60), nullable=False),
        sa.Column('password', sa.String(30), nullable=False)
    )


def downgrade():
    op.drop_table('users')
