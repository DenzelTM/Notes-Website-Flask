import email
from time import timezone
from . import db # this imports the object DB from the current website package file.
from flask_login import UserMixin
from sqlalchemy.sql import func #this is for getting the current date and time.

class Note(db.Model):
  id = db.column(db.Integer, primary_key= True)
  text = db.column(db.string(10000))
  date = db.column(db.DateTime(timezone = True), default=func.now)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
  id = db.Column(db.Integer , primary_key=True) #this is our primary key
  email = db.Column(db.String(50) , unique=True)
  password = db.Column(db.String(50))
  first_name = db.column(db.String(50))
  notes = db.relationship('Note')