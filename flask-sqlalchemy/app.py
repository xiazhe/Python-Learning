from flask import Flask
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Error  application not registered on db instance and no application bound to current context
# def create_app():
#     db.init_app(app)
#     db.create_all()
#     return app

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()