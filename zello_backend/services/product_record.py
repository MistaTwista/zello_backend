import sqlalchemy as sa
from paginate_sqlalchemy import SqlalchemyOrmPage
from ..models.product import Product

class ProductRecordService(object):


    @classmethod
    def all(cls, request):
        query = request.dbsession.query(Product)
        return query.order_by(sa.desc(Product.created))


    @classmethod
    def by_id(cls, _id, request):
        query = request.dbsession.query(Product)
        return query.get(_id)

    @classmethod
    def delete_by_id(cls, _id, request):
        query = request.dbsession.query(Product)
        # session.delete(jack)
        return query.delete(_id)


    @classmethod
    def get_paginator(cls, request, page=1):
        query = request.dbsession.query(Product)
        query = query.order_by(sa.desc(Product.created))
        query_params = request.GET.mixed()

        def url_maker(link_page):
            query_params['page'] = link_page
            return request.current_route_url(_query=query_params)

        return SqlalchemyOrmPage(query, page, items_per_page=5,
                                url_maker=url_maker)


