from app_init import db 

class Shelf(db.Model):
    shelf_id = db.Column(db.Integer, primary_key=True)
    manager = db.Column(db.String(50))
    location = db.Column(db.String(50), unique=True)

    items = db.relationship("Item", back_populates="shelf")


class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Integer)
    shelf_id = db.Column(db.ForeignKey("shelf.shelf_id"))

    shelf = db.relationship("Shelf", back_populates="items")