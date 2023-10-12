"""first

Revision ID: d4f7c22d70f0
Revises: 
Create Date: 2023-10-12 00:26:04.675045

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd4f7c22d70f0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('price_usd', sa.Integer(), nullable=True),
    sa.Column('odometer', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('phone_number', sa.BigInteger(), nullable=True),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('images_count', sa.Integer(), nullable=True),
    sa.Column('car_number', sa.String(), nullable=True),
    sa.Column('car_vin', sa.String(), nullable=True),
    sa.Column('datetime_found', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cars')
    # ### end Alembic commands ###
