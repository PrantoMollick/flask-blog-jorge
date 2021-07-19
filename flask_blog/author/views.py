from flask import render_template, redirect, url_for, request
from flask_blog import app
from flask_blog.author.form import RegisterForm
from functools import wraps


@app.route('/login')
def login():
    return "login"


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('author/register.html', form= form), 200


@app.route('/success')
def success():
    return 'Author registered';