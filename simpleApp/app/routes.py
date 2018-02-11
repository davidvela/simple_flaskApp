from flask import render_template, flash, redirect, url_for
# from flask import *
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index2')
def index():
    userB = {'username': 'David_B'}
    userA = {'username': 'David_A'}
    # return "Hello, World!"
    # return render_template('index.html', title='Home', user=user)
    
    post1 = {'author': userB, 'body': "Hola que tal"    }
    post2 = {'author': userA, 'body': "Muy bien y tu?"  }
    posts = [post1, post2]

    return render_template('index2.html', title='Home', user=userB, posts = posts)


# @app.route('/login') #no logic for the button. 
# def login():
#     form = LoginForm()
#     return render_template('login.html', title='Sign In', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():  # press button
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        # return redirect('/index2')
        return redirect(url_for('index'))
    form.username.data = "user"
    form.password.data = "pass"
    return render_template('login.html', title='Sign In', form=form)