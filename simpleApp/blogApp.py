from flask import *
import pandas as pd

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'David_A'}
    return render_template('index.html', title='Home', user=user)
    #return "Hello, World!"


@app.route('/hello')
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)  
    # app.run(host="0.0.0.0")  # accessible from the network! 
