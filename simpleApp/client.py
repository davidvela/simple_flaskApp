from flask import *
import pandas as pd
from requests import put, get

app = Flask(__name__)
app.config['SERVER_NAME'] = '127.0.0.1' + ':' + '5002'
# flask_app.config['SERVER_NAME'] = server_name + ':' + server_port
# flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION # 'list'
# flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE # True
# flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER # False
# flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP # False 
#                   - If a request does not match any of the application endpoints => return error 404 or not 


@app.route('/')
@app.route('/index')
def index():
    # user = {'username': 'David_A'}
    # return render_template('index.html', title='Home', user=user)
    # print(get('http://localhost:5000/hello').json())
    # return "Hello, World!"
    ret = get('http://localhost:5000/hello').json()
    print(ret)
    return "hello__" + ret["hello"] #"Hello, World!"
    


if __name__ == "__main__":
    app.run(debug=True)  