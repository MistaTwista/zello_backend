import datetime
import decimal
from marshmallow import Schema
from pyramid.renderers import JSON


class RenderSchema(Schema):
    """
    Schema to prevent marshmallow from using its default type mappings.

    We use this schema for rendering output: For those cases we don't want
    marshmallow's default type mappings. We want Pyramid's JSON-rendering
    functionality instead, where we already have some json-adapers.
    """

    TYPE_MAPPING = {}


def custom_json_renderer():
    """
    Return a custom json renderer that can deal with some datetime objects.
    """


    def datetime_adapter(obj, request):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        raise TypeError ("DateTime is not serializable")


    def time_adapter(obj, request):
        if isinstance(obj, datetime.date):
            return str(obj)
        raise TypeError ("Time is not serializable")


    def decimal_adapter(obj, request):
        if isinstance(obj, decimal.Decimal):
            return float("{0:.2f}".format(obj))
        raise TypeError ("Decimal not serializable")


    json_renderer = JSON()
    json_renderer.add_adapter(datetime.datetime, datetime_adapter)
    json_renderer.add_adapter(datetime.date, time_adapter)
    json_renderer.add_adapter(datetime.time, time_adapter)
    json_renderer.add_adapter(decimal.Decimal, decimal_adapter)
    return json_renderer
