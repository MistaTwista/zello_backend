import datetime
from zello_backend.models.meta import Base
import sqlalchemy as sa
import sqlalchemy.orm as orm


class Product(Base):
    __tablename__ = 'product'
    id = sa.Column(sa.Integer, primary_key=True)
    selling_id = sa.Column(sa.Integer, sa.ForeignKey('selling.id'))
    name = sa.Column(sa.Unicode(255), unique=False, nullable=False)
    price = sa.Column(sa.Numeric(12, 2), nullable=False)
    quantity = sa.Column(sa.Float)
    created = sa.Column(sa.DateTime, default=datetime.datetime.utcnow)

    selling = orm.relationship("Selling", back_populates="products")

    def __json__(self, request):
        return {
            'id': self.id,
            'selling_id': self.selling_id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'created': self.created,
        }

    def __repr__(self):
        return "<Product(name='%s')>" % self.name
