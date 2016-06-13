import sqlalchemy as sa
from paginate_sqlalchemy import SqlalchemyOrmPage
from ..models.selling import Selling

class SellingRecordService(object):


    def __json__(self, request):
        return {'code': self.code}


    @classmethod
    def all(cls, request):
        query = request.dbsession.query(Selling)
        return query.order_by(sa.desc(Selling.created))


    @classmethod
    def by_id(cls, _id, request):
        query = request.dbsession.query(Selling)
        return query.get(_id)


    @classmethod
    def get_paginator(cls, request, page=1):
        query = request.dbsession.query(Selling)
        query = query.order_by(sa.desc(Selling.created))
        query_params = request.GET.mixed()

        def url_maker(link_page):
            query_params['page'] = link_page
            return request.current_route_url(_query=query_params)

        return SqlalchemyOrmPage(query, page, items_per_page=5,
                                url_maker=url_maker)


