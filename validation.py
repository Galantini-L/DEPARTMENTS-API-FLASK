from dataclasses import fields
import json
from marshmallow import Schema, fields, ValidationError, validate


class Validation_departmentsData(Schema):
    id = fields.Integer()
    name = fields.String(validate=validate.Length(max=30))
    price = fields.Float()
    department = fields.String(validate=validate.Length(max=30))

def val_deptData(data):
    try:
        #deserializing
        product_load = Validation_departmentsData().load(data)
        print('successful data validation')
        return json.dumps(product_load)
    except ValidationError as err:
        print(err.messages)
        print(err.valid_data)
        raise err


# no_valData= {
#     "department":"Outdoors",
#     "id":1,
#     "name":"Modern Granite Pants",
#     "price":817.00}
# validated = val_dataProduct(no_valData)
# print(type(validated))


    