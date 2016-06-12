import datetime
from zello_backend.models.meta import Base
import sqlalchemy as sa
import sqlalchemy.orm as orm


class Selling(Base):
    __tablename__ = 'selling'
    id = sa.Column(sa.Integer, primary_key=True)
    code = sa.Column(sa.Unicode(255), unique=True, nullable=False)
    summ = sa.Column(sa.Numeric(12, 2), nullable=False)
    created = sa.Column(sa.DateTime, default=datetime.datetime.utcnow)
    products = orm.relationship("Product", order_by="Product.id")
