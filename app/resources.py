from flask import request
from flask_restx import Resource, Namespace 

from api_models import item_input_model, item_model_a, item_update_model, shelf_model, shelf_input_model
from app_init import db
from models import Shelf, Item

wh = Namespace("Warehouse")

items = []

@wh.route('/shelf')
class Shelf_route(Resource):
    @wh.marshal_with(shelf_model)
    def get(self):
        shelf_id = request.args.get('shelf_id', type=int)
        if shelf_id is None:
            shelves= Shelf.query.all()
            for shelf in shelves:
                print(shelf.shelf_id, shelf.manager, shelf.location)
            return Shelf.query.all()
        return Shelf.query.get(shelf_id)
    
    @wh.expect(shelf_input_model)
    @wh.marshal_with(shelf_model)
    def post(self):
        shelf = Shelf(
            manager=wh.payload['manager'],
            location=wh.payload['location']
        )
        db.session.add(shelf)
        db.session.commit()
        return shelf, 201
    
    @wh.expect(shelf_input_model)
    @wh.marshal_with(shelf_model)
    def put(self):
        shelf_id = request.args.get('shelf_id', type=int)
        shelf = Shelf.query.get(shelf_id)
        shelf.manager = wh.payload["manager"]
        db.session.commit()
        return shelf

    def delete(self):
        shelf_id = request.args.get('shelf_id', type=int)
        shelf = Shelf.query.get(shelf_id)
        db.session.delete(shelf)
        db.session.commit()
        return {}, 204


@wh.route('/item')
class Item_route(Resource):
    @wh.marshal_with(item_model_a)
    def get(self):
        item_id = request.args.get('item_id', type=int)
        if item_id is None:
            items = Item.query.all()
            for item in items:
                print(item.item_id, item.name, item.price, item.shelf_id)
            return Item.query.all()
        return Item.query.get(item_id)
    
    @wh.expect(item_input_model)
    @wh.marshal_with(item_model_a)
    def post(self):
        item = Item(
            name=wh.payload['name'],
            price=wh.payload['price'],
            shelf_id=wh.payload['shelf_id']
        )
        db.session.add(item)
        db.session.commit()
        return item, 201
    
    @wh.expect(item_update_model)
    @wh.marshal_with(item_model_a)
    def put(self):
        item_id = request.args.get('item_id', type=int)
        item = Item.query.get(item_id)
        item.price = wh.payload['price']
        item.shelf_id = wh.payload['shelf_id']
        db.session.commit()
        return item

    def delete(self):
        item_id = request.args.get('item_id', type=int)
        item = Item.query.get(item_id)
        db.session.delete(item)
        db.session.commit()
        return {}, 204