from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        user_email = User.query.filter_by(email=email).first()
        user_name = User.query.filter_by(username=username).first()

        if user_email:
            flash('Email already exist.', category='error')

        elif user_name:
            flash('Username already exist.', category='error')

        elif len(username) < 2:
            flash('Username must be at least 2 character long', category='error')

        elif len(email) < 4:
            flash('Email is not valid.', category='error')

        elif len(password) < 7:
            flash('Password must be at least 7 characters long', category='error')

        else:
            new_user = User(username=username, email=email, password=generate_password_hash(password, method='scrypt'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            flash('Account created', category='success')

            return redirect(url_for('views.home'))

    return render_template('register.html', user=current_user)

@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully !', category='success')
                login_user(user)
                return redirect(url_for('views.home'))
            else:
                flash('Wrong password, try again.', category='error')
        else:
            flash('Username does not exist.', category='error')

    return render_template('login.html', user=current_user)

@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))