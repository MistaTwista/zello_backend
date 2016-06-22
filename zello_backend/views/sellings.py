from pyramid.view import view_config, notfound_view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from ..models.selling import Selling
from ..models.product import Product
from ..services.selling_record import SellingRecordService
from ..forms import SellingCreateForm, SellingUpdateForm
from ..forms import ProductCreateForm, ProductUpdateForm
from pyramid.renderers import JSON
import datetime

def cl(message):
    print("--------=========================--------")
    print("--------============" + message + "=============--------")
    print("--------=========================--------")


@view_config(route_name='sellings_json', renderer='json')
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


@view_config(route_name='selling_json', renderer='json', request_method='GET')
def get_selling_view(request):
    cl("SELLING_VIEW")
    selling = get_selling(request)
    if not selling:
        return HTTPNotFound()
    return {'selling': selling}


@view_config(route_name='selling_json', renderer='json', request_method='POST')
def post_selling_view(request):
    cl("POST_SELLING_VIEW")
    selling = get_selling(request)
    product = Product()
    form = ProductCreateForm(request.POST, obj=product)
    if form.validate():
        form.populate_obj(product)
        request.dbsession.add(product)
    if not selling:
        return HTTPNotFound()
    return {'selling': selling}


@view_config(route_name='selling_json', renderer='json', request_method='DELETE')
def delete_product(request):
    cl("DELETE_PRODUCT")
    selling = get_selling(request)
    return Response(
        status='202 Accepted',
        content_type='application/json; charset=UTF-8')


def get_selling(request):
    selling_id = int(request.matchdict.get('selling_id', -1))
    return SellingRecordService.by_id(selling_id, request)
