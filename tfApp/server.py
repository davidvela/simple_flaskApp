from flask import *
from flask_restplus import Api, Resource, reqparse
from flask_cors import CORS  
# #https://github.com/corydolphin/flask-cors/issues/201

app = Flask(__name__)
api = Api(app)
CORS(app)

@api.route('/hello') 
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

if __name__ == '__main__':
    # app.run(debug=True) # Debug mode should never be used in a production environment!
    app.run(host='0.0.0.0')