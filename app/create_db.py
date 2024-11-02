from app_init import app, db
from models import Item, Shelf

with app.app_context():
    db.drop_all()
    db.create_all()

print("Database tables created.")