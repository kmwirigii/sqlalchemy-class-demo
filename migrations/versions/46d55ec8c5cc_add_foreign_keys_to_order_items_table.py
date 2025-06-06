"""add foreign keys to order items table

Revision ID: 46d55ec8c5cc
Revises: 796dd9ee7fea
Create Date: 2025-05-28 09:58:01.019863

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46d55ec8c5cc'
down_revision: Union[str, None] = '796dd9ee7fea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('customers', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_customers_email'), ['email'])
        batch_op.create_unique_constraint(batch_op.f('uq_customers_phone'), ['phone'])

    with op.batch_alter_table('order_items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('order_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('product_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_order_items_product_id_products'), 'products', ['product_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_order_items_order_id_orders'), 'orders', ['order_id'], ['id'])

    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_orders_order_id'), ['order_id'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_orders_order_id'), type_='unique')

    with op.batch_alter_table('order_items', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_order_items_order_id_orders'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_order_items_product_id_products'), type_='foreignkey')
        batch_op.drop_column('product_id')
        batch_op.drop_column('order_id')

    with op.batch_alter_table('customers', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_customers_phone'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_customers_email'), type_='unique')

    # ### end Alembic commands ###
