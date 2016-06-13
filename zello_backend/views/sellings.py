from pyramid.view import view_config, notfound_view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from ..models.selling import Selling
from ..services.selling_record import SellingRecordService
from ..forms import SellingCreateForm, SellingUpdateForm
from pyramid.renderers import JSON
import datetime


@view_config(route_name='sellings_json', renderer='json')
@view_config(route_name='sellings_json_', renderer='json')
def sellings_view(request):
    sellings = SellingRecordService.all(request)
    return {'sellings': sellings.all()}


@view_config(route_name='selling_json', renderer='json')
def selling_view(request):
    selling_id = int(request.matchdict.get('selling_id', -1))
    selling = SellingRecordService.by_id(selling_id, request)
    if not selling:
        return HTTPNotFound()
    return {'selling': selling}


@view_config(route_name='sellings_action', match_param='action=create',
             renderer='json')
def selling_create(request):
    selling = Selling()
    form = SellingCreateForm(request.POST)
    if request.method == 'POST':
        form.populate_obj(selling)
        request.dbsession.add(selling)
        return {'selling': selling}
