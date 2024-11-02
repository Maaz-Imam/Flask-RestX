from flask_restx import fields

from app_init import api

item_input_model = api.model('Item', {
    'name': fields.String,
    'price': fields.Float,
    'shelf_id': fields.Integer
})

item_model_a = api.model('Item', {
    'item_id': fields.Integer,
    'name': fields.String,
    'price': fields.Float,
    'shelf_id': fields.Integer
})

item_model_b = api.model('Item', {
    'item_id': fields.Integer,
    'name': fields.String,
    'price': fields.Float,
})

item_update_model = api.model('Item', {
    'price': fields.Float,
    'shelf_id': fields.Integer
})

shelf_input_model = api.model('ShelfInput', {
    'manager': fields.String,
    'location': fields.String
})

shelf_model = api.model('Shelf', {
    'shelf_id': fields.Integer,
    'manager': fields.String,
    'location': fields.String,
    'items': fields.List(fields.Nested(item_model_b))
})