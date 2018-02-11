from flask import Flask, request
from flask_restplus import Api, Resource, reqparse

app = Flask(__name__)

#initialize it with an application object
api = Api(app) 

# lazily  initialization
# api = Api()
# api.init_app(app)

#minimal API
# api.add_resource(HelloWorld, '/hello', '/world')

# @api.route('/hello')
@api.route('/hello', '/world') # multiple routes / Endpoints 
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
        # return {'task': 'Hello world'}       # default to 200 OK 
        # return {'task': 'Hello world'}, 201  # Response code to 201
        # return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'} # Response code to 201 + custom header

# Basic CRUD resource: toDo
todos = {}
@api.route('/<string:todo_id>')
# api.add_resource(Todo, '/todo/<int:todo_id>', endpoint='todo_ep')
# @api.route('/todo/<int:todo_id>', endpoint='todo_ep')
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

# validation 
rate = 0 
@api.route('/rate')
class Rate(Resource):
    def get(self):
        return {'rate': rate }
    def post(self, rate_val ):
        rate = rate_val
        return rate
        # parser = reqparse.RequestParser()
        # parser.add_argument('rate', type=int, help='Rate to charge for this resource')
        # args = parser.parse_args()
        # args = parser.parse_args(strict=True)



if __name__ == '__main__':
    app.run(debug=True) # Debug mode should never be used in a production environment!

def test_curl():
    pass
    # testing - HelloWorld: 
    # curl http://127.0.0.1:5000/hello
    # Swagger UI - 

    # testing - toDo:
    # $ curl http://localhost:5000/todo1 -d "data=Remember the milk" -X PUT
    # $ curl http://localhost:5000/todo1
    # $ curl http://localhost:5000/todo2 -d "data=Change my brakepads" -X PUT
    # $ curl http://localhost:5000/todo2

    # testing - validation:
    # $ curl -d 'rate=foo' http://127.0.0.1:5000/todos -> {'status': 400, 'message': 'foo cannot be converted to int'}
    #hi