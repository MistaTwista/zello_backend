from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from ..models.selling import Selling
from ..services.selling_record import SellingRecordService
from pyramid.renderers import JSON
import datetime


@view_config(route_name='sellings_json', renderer='json')
@view_config(route_name='sellings',
             renderer='zello_backend:templates/sellings.jinja2')
def sellings_view(request):
    page = int(request.params.get('page', 1))
    sellings = SellingRecordService.all(request)
    return {'sellings': sellings}


@view_config(route_name='selling', renderer='json')
def selling_view(request):
    selling_id = int(request.matchdict.get('id', -1))
    entry = SellingRecordService.by_id(selling_id, request)
    if not entry:
        return HTTPNotFound()
    return {'entry': entry}


@view_config(route_name='user_basic', renderer='json')
def get_user_basic(request):
    return {
        "id": 1,
        "name": "Bruce Wayne",
        "super_hero": True,
        "friend_ids": [2, 3, 5, 8],
        "created_at": datetime.datetime(2015, 1, 23, 16, 2, 15),
    }
