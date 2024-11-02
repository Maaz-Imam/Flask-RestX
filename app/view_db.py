from app_init import app, db
from models import Item, Shelf

with app.app_context():
    print(f"{'Item ID':<10} {'Name':<30} {'Price':<10} {'Shelf ID':<10}")
    print("-" * 60)
    items = Item.query.all()
    for item in items:
        print(f"{item.item_id:<10} {item.name:<30} {item.price:<10} {item.shelf_id:<10}")

    print("\n")
    print(f"{'Shelf ID':<10} {'Manager':<30} {'Location':<30}")
    print("-" * 70)
    shelves = Shelf.query.all()
    for shelf in shelves:
        print(f"{shelf.shelf_id:<10} {shelf.manager:<30} {shelf.location:<30}")