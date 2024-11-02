# Flask-RestX
Testing API handling using Flask RestX

This mini-project is connected to SQLite3 which serves as the database.

## In /app:
- app_init.py: Initializes the Flask App and SQLite3 Database.
- models.py: Describes the tables and their respective columns for the Database.
- create_db.py: Used to create all the tables using the models from models.py.
- view_db.py: For printing the tables data to the console for viewing.
- api_models.py: Contains all Formats and constraints of how to post, update and delete the table's data.
- resources.py: Contains all the App routes and APIs (GET, POST, PUT, DELETE).
- main.py: Runs the Flask App.

## The APIs can:
- POST data of shelf and items to server
- GET data of specific Shelves and their items
- GET list of all shelves and items
- GET data of specific item
- When an item is POST-ed it is automatically added to it's corresponding Shelf list.
