from app_init import app, api
from resources import wh

api.add_namespace(wh)

if __name__ == '__main__':
    app.run(debug=True)