from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
db = SQLAlchemy(app)
# 定义User类
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    # public_id = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    # admin = db.Column(db.Boolean)

    def __repr__(self):
        return f"<Parent {self.name}>"

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "username": self.username,
    #         "public_id": self.public_id,
    #         "password": self.password,
    #         "admin": self.admin,
    #     }

