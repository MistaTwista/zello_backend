from pyramid.view import view_config, notfound_view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from ..models.selling import Selling
from ..models.product import Product
from ..services.product_record import ProductRecordService
from ..forms import SellingCreateForm, SellingUpdateForm
from ..forms import ProductCreateForm, ProductUpdateForm
from pyramid.renderers import JSON
from pyramid.response import Response
import datetime

def cl(message):
    print("--------=========================--------")
    print("--------============" + message + "=============--------")
    print("--------=========================--------")


@view_config(route_name='products_json', renderer='json', request_method='POST')
def create_product(request):
    cl("POST_CREATE_PRODUCT")
    # selling = get_selling(request)
    product = Product()
    form = ProductCreateForm(request.POST, obj=product)
    if form.validate():
        form.populate_obj(product)
        request.dbsession.add(product)
        return {'product': product}
    return HTTPNotFound()


@view_config(route_name='product_json', renderer='json', request_method='DELETE')
def delete_product(request):
    cl("DELETE_PRODUCT")
    # selling = get_selling(request)
    product = delete_product(request)
    return Response(status='delete',
        content_type='application/json; charset=UTF-8')


def delete_product(request):
    product_id = int(request.matchdict.get('product_id', -1))
    return ProductRecordService.delete_by_id(product_id, request)


# def get_selling(request):
#     selling_id = int(request.matchdict.get('selling_id', -1))
#     return SellingRecordService.by_id(selling_id, request)
