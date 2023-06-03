from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()


class Facts(db.Model):
    __tablename__ = "facts"
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(250))
    facts = db.Column(db.Text)