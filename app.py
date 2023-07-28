#importaciones 
from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

#incializar objeto flask 
app=Flask(__name__)
app.config.from_object(Config)

#inicializar el objeto SQLALCHEMY 
db=SQLAlchemy(app)
Migrate= Migrate(app, db)

# modelos - entidaded del proyecto

class Cliente(db.Model):
    __tablename__="clientes"
    id= db.Column(db.Integer, primary_key= True )
    username=db.Column(db.String(100), unique = True)
    password=db.Column(db.String(200))
    email=db.Column(db.String(100), unique = True)
    
    

    
    



