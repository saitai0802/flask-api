from datetime import timedelta

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity

from security import authenticate, identity # our security.py file

app = Flask(__name__)

# For more JWT setting:
# http://blog.tecladocode.com/learn-python-advanced-configuration-of-flask-jwt/
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800) # config JWT to expire within half an hour
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'this is a testing enviroment' # Don't put your secret key on your IDE in Production enviroment.

api = Api(app) # We use Api() to add flask_restful.Resource easily
jwt = JWT(app, authenticate, identity)

items = []

class Item(Resource):

    # That's going to parse the arguments that come through the JSON payload and verify it
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        # We use next to get the first item we found by filter function
        return {'item': next(filter(lambda x: x['name'] == name, items), None)} # If next can't find any, return None.

    def post(self, name):

        # If item exsist, return item.
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists.".format(name)}

        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item

    @jwt_required()
    def delete(self, name):
        global items # get the outer items object
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    @jwt_required()
    def put(self, name):

        # All the value we didn't declare at the beginning of this Class will be erased.
        data = Item.parser.parse_args()

        # Once again, print something not in the args to verify everything works
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}

# We don't need to decorate by ourselves
api.add_resource(Item, '/item/<string:name>') # http://localhost:5000/student/Sai
api.add_resource(ItemList, '/items')

if __name__ == '__main__':
    #app.run(debug=True)  # important to mention debug=True
    app.run(host = '0.0.0.0', port=5000, debug=True)
