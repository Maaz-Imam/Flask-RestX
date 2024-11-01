from flask import request
from flask_restx import Resource, Namespace 

from api_models import item_input_model, shelf_model, shelf_input_model

wh = Namespace("Warehouse")

shelf = []
items = []

@wh.route('/shelf')
class Shelf(Resource):
    @wh.marshal_with(shelf_model)
    def get(self):
        shelf_id = request.args.get('shelf_id', type=int)
        if shelf_id is None:
            return shelf
        return [item for item in shelf if item["shelf_id"] == shelf_id][0]
    
    @wh.expect(shelf_input_model)
    @wh.marshal_with(shelf_model)
    def post(self):
        shelf_id = len(shelf) + 1
        shelf_data = wh.payload
        shelf_data['shelf_id'] = shelf_id
        shelf_data['items'] = []
        shelf.append(shelf_data) 
        return shelf_data, 201

@wh.route('/item/<int:item_id>')
class Item(Resource):
    @wh.marshal_with(item_input_model)
    def get(self, item_id):
        return [item for item in items if item["item_id"] == item_id][0]
    
    @wh.expect(item_input_model)
    @wh.marshal_with(item_input_model)
    def post(self, item_id):
        item_data = wh.payload
        item_data['item_id'] = item_id
        items.append(item_data)
        shelf_id = int(item_data['shelf_id'])
        for target_shelf in shelf:
            if target_shelf['shelf_id'] == shelf_id:
                target_shelf['items'].append({
                "item_id": item_data["item_id"],
                "name": item_data["name"],
                "price": item_data["price"]
            }) 
        return item_data, 201