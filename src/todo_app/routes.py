from flask import render_template, request, redirect, url_for, flash, abort
from . import db
from .models import Todo

def register_routes(app):

    @app.route('/')
    def index():
        tasks = db.session.query(Todo).all()
        return render_template('index.html', tasks=tasks)

    @app.route('/add', methods=['POST'])
    def add():
        task_content = request.form['task']
        if task_content.strip():
            new_task = Todo(task=task_content)
            db.session.add(new_task)
            db.session.commit()
            flash("Task added successfully", "success")
        else:
            flash("Task cannot be empty", "danger")
        return redirect(url_for('index'))

    @app.route('/delete/<int:id>')
    def delete(id):
        task = db.session.get(Todo, id)
        if task is None:
            abort(404)
        db.session.delete(task)
        db.session.commit()
        flash("Task deleted", "info")
        return redirect(url_for('index'))

    @app.route('/toggle/<int:id>')
    def toggle(id):
        task = db.session.get(Todo, id)
        if task is None:
            abort(404)
        task.done = not task.done
        db.session.commit()
        flash("Task updated", "warning")
        return redirect(url_for('index'))
