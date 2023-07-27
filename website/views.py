from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

from .models import Task
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        status = request.form.get('status')

        if len(title) < 1:
            flash('Title is too short.', category='error')
        elif len(description) < 1 :
            flash('Description is too short.', category='error')
        else:
            new_task = Task(title=title, description=description, status=status, user_id=current_user.id)
            db.session.add(new_task)
            db.session.commit()
            flash('Task added !', category='succes')

    return render_template('home.html', user=current_user)

@views.route('/delete/<int:id>')
def delete_task(id):

    task = Task.query.get(id)
    if task:
        if task.user_id == current_user.id:
            db.session.delete(task)
            db.session.commit()

    return redirect(url_for('views.home'))