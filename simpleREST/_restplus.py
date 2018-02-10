from flask import Flask, request
from flask_restplus import Api, Resource

app = Flask(__name__)

#initialize it with an application object
api = Api(app) 

# lazily  initialization
# api = Api()
# api.init_app(app)

#minimal API
@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

# Basic CRUD resource: toDo
todos = {}
@api.route('/<string:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


if __name__ == '__main__':
    app.run(debug=True) # Debug mode should never be used in a production environment!

# testing - HelloWorld: 
# curl http://127.0.0.1:5000/hello
# Swagger UI - 

# testing - HelloWorld: 
