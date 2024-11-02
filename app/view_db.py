from app_init import app, db
from models import Item, Shelf

with app.app_context():
    print('here')
    items = Item.query.all()
    for item in items:
        print(item.item_id, item.name, item.price, item.shelf_id)

    shelves= Shelf.query.all()
    for shelf in shelves:
        print(shelf.shelf_id, shelf.manager, shelf.location)