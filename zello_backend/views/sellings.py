from pyramid.view import view_config, notfound_view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from ..models.selling import Selling
from ..models.product import Product
from ..services.selling_record import SellingRecordService
from ..forms import SellingCreateForm, SellingUpdateForm
from ..forms import ProductCreateForm, ProductUpdateForm
from pyramid.renderers import JSON
import datetime


@view_config(route_name='sellings_json', renderer='json')
@view_config(route_name='sellings_json_', renderer='json')
@view_config(route_name='sellings_json', match_param='action=create',
             renderer='json')
def sellings_view(request):
    selling = Selling()
    form = SellingCreateForm(request.POST, obj=selling)
    if request.method == 'POST' and form.validate():
        form.populate_obj(selling)
        request.dbsession.add(selling)
    sellings = SellingRecordService.all(request)
    return sellings.all()


@view_config(route_name='selling_json', renderer='json')
@view_config(route_name='selling_json', match_param='action=create',
             renderer='json')
def selling_view(request):
    selling_id = int(request.matchdict.get('selling_id', -1))
    selling = SellingRecordService.by_id(selling_id, request)
    product = Product()
    form = ProductCreateForm(request.POST, obj=product)
    if request.method == 'POST' and form.validate():
        form.populate_obj(product)
        request.dbsession.add(product)
    if not selling:
        return HTTPNotFound()
    return {'selling': selling}
