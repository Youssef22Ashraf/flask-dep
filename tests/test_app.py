import sys, os 
import pytest
from todo_app import create_app, db
from todo_app.models import Todo

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

@pytest.fixture
def client():
    """Set up a test client with an in-memory SQLite database"""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # in-memory DB
    app.config['WTF_CSRF_ENABLED'] = False  # disable CSRF for testing

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()


def test_homepage_loads(client):
    """Test that homepage loads correctly"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"My To-Do List" in response.data


def test_add_task(client):
    """Test adding a new task"""
    response = client.post('/add', data={'task': 'Test Task'}, follow_redirects=True)
    assert b"Task added successfully" in response.data
    assert b"Test Task" in response.data


def test_toggle_task(client):
    """Test toggling a task"""
    # Add a task first
    client.post('/add', data={'task': 'Toggle Task'}, follow_redirects=True)
    task = Todo.query.first()
    assert task.done is False

    # Toggle it
    response = client.get(f'/toggle/{task.id}', follow_redirects=True)
    assert b"Task updated" in response.data
    toggled_task = db.session.get(Todo, task.id)  # modern SQLAlchemy
    assert toggled_task.done is True


def test_delete_task(client):
    """Test deleting a task"""
    # Add a task first
    client.post('/add', data={'task': 'Delete Me'}, follow_redirects=True)
    task = Todo.query.first()
    assert task is not None

    # Delete it
    response = client.get(f'/delete/{task.id}', follow_redirects=True)
    assert b"Task deleted" in response.data
    assert b"Delete Me" not in response.data
