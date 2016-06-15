from wtforms import (
    Form,
    StringField,
    TextAreaField,
    DecimalField,
    FloatField,
    IntegerField,
    DateField,
    HiddenField,
    validators,
)

strip_filter = lambda x: x.strip() if x else None


class BlogCreateForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=255)],
                        filters=[strip_filter])
    body = TextAreaField('Contents', [validators.Length(min=1)],
                        filters=[strip_filter])


class BlogUpdateForm(BlogCreateForm):
    id = HiddenField()


class SellingCreateForm(Form):
    code = StringField('code', [validators.Length(min=1, max=255)],
                        filters=[strip_filter])
    # created = DateField('created')
    # summ = DecimalField('summ')


class SellingUpdateForm(SellingCreateForm):
    id = HiddenField()


class ProductCreateForm(Form):
    name = StringField('name', [validators.Length(min=1, max=255)],
                        filters=[strip_filter])
    selling_id = IntegerField('selling_id')
    quantity = FloatField('quantity')
    price = DecimalField('price')


class ProductUpdateForm(ProductCreateForm):
    id = HiddenField()
