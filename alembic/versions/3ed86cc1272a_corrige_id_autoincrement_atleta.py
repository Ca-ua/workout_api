"""corrige id autoincrement atleta

Revision ID: 3ed86cc1272a
Revises: d2a906642dc7
Create Date: 2025-04-07 00:29:58.459025

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3ed86cc1272a'
down_revision: Union[str, None] = 'd2a906642dc7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
