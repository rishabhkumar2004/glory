"""create_main_tables
 
Revision ID: 81471b27736e
Revises: 
Create Date: 2023-12-14 15:55:57.499391
 
"""
from alembic import op
import sqlalchemy as sa

 
# revision identifiers, used by Alembic
revision = '81471b27736e'
down_revision = None
branch_labels = None
depends_on = None
 
def create_tables() -> None:
    op.create_table(
        "skills",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False, index=True),
        sa.Column("contact_info", sa.Text, nullable=True),
        sa.Column("test_data", sa.Integer, nullable=True)
    )
 
def upgrade() -> None:
    create_tables()
 
 
def downgrade() -> None:
    op.drop_table("skills")
 
