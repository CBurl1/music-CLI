"""initial migration

Revision ID: 67cb4f637077
Revises: 
Create Date: 2023-03-30 08:04:33.223764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67cb4f637077'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('listeners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('songs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('artist', sa.String(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('streams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('song_name', sa.String(), nullable=True),
    sa.Column('song_id', sa.Integer(), nullable=True),
    sa.Column('listener_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['listener_id'], ['listeners.id'], ),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('streams')
    op.drop_table('songs')
    op.drop_table('listeners')
    # ### end Alembic commands ###
