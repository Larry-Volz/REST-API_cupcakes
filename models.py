"""Models for Cupcake app.""" 
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

def connect_db(app):
    db.app = app 
    db.init_app(app)

#MODELS GO BELOW
class Cupcake (db.Model):  #inherits from db
   """ Cupcake info """
   __tablename__ = "cupcakes"
   def __repr__(self):
       return f"id={self.id} flavor={self.flavor} size={self.size} rating={self.rating} "  #for better referencing

   id = db.Column(db.Integer, primary_key = True, autoincrement = True)
   flavor = db.Column(db.Text, nullable = False, unique = False)
   size = db.Column(db.Text, nullable = False, default = "medium")
   rating = db.Column(db.Float, nullable = False)
   image = db.Column(db.Text, nullable = False, default = "https://tinyurl.com/demo-cupcake")


