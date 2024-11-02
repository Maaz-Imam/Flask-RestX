# Flask-RestX
Testing API handling using Flask RestX

This mini-project is connected to SQLite3 which serves as the database.

## In /app:
- app_init.py: Initializes the Flask App and SQLite3 Database.
- models.py: Describes the tables and their respective columns for the Database.
- create_db.py: Used to create all the tables using the models from models.py.
- view_db.py: For printing the table's data to the console for viewing.
- api_models.py: Contains all Formats and constraints of how to post, update and delete the table's data.
- resources.py: Contains all the App routes and APIs (GET, POST, PUT, DELETE).
- main.py: Runs the Flask App.

## The APIs can:
- POST data of shelf and items to server
- GET data of specific Shelves and their items
- GET list of all shelves and items
- GET data of specific item
- When an item is POST-ed it is automatically added to it's corresponding Shelf list.

### Sample Bash commands for querying the database:
- Posting to Shelf table:
![image](https://github.com/user-attachments/assets/176a784a-88cc-4abb-85e1-0e7fee16befc)
$ curl http://127.0.0.1:5000/Warehouse/shelf -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{"manager": "Ali, "location": "top-left"}' -X POST


- Posting to Item table:
![image](https://github.com/user-attachments/assets/f6d1ead7-b272-4b72-b188-88a57fae9aaa)
$ curl http://localhost:5000/Warehouse/item -H 'accept: application/json'   -H 'Content-Type: application/json' -d '{"name": "bottle", "price": "250", "shelf_id": "1"}' -X POST
