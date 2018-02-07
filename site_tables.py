from flask import *
import pandas as pd
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

# @app.route('/index2')
# def login(client, username, password):
#     return client.post('/login', data=dict(
#         username=username,
#         password=password
#     ), follow_redirects=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route("/tables")
def show_tables():
    data = pd.read_excel('dummy_data.xlsx')
    data.set_index(['Name'], inplace=True)
    data.index.name=None
    females = data.loc[data.Gender=='f']
    males = data.loc[data.Gender=='m']
    #print(males)
    return render_template('view.html',
            tables=[females.to_html(classes='female'), males.to_html(classes='male')],
            titles = ['na', 'Female surfers', 'Male surfers'])

if __name__ == "__main__":
    app.run(debug=True)    
    # app.run(host='0.0.0.0', port=80)
