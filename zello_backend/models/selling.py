import datetime
from zello_backend.models.meta import Base
import sqlalchemy as sa
import sqlalchemy.orm as orm
import json


class Selling(Base):
    __tablename__ = 'selling'
    id = sa.Column(sa.Integer, primary_key=True)
    code = sa.Column(sa.Unicode(255), unique=True, nullable=False)
    summ = sa.Column(sa.Numeric(12, 2), default=0)
    created = sa.Column(sa.DateTime, default=datetime.datetime.utcnow)
    products = orm.relationship( "Product", order_by="Product.id",
        back_populates="selling",
        cascade="all, delete, delete-orphan")


    def __repr__(self):
        return json.dumps({
            'id': self.id,
            'code': self.code,
            'summ': self.summ,
            'created': self.created,
            'products': self.products,
        })


    def __json__(self, request):
        return {
            'id': self.id,
            'code': self.code,
            'summ': self.summ,
            'date': self.created,
            'products': self.products,
        }
