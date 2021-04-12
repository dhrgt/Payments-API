from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #instantiate database

class CustomersModel(db.Model): #create database model for customers object
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=True)

    def __init__(self, name, price, author):
        self.name = name
        self.address = address
        self.phone = author
        self.email = email
        self.description = description

    def json(self):
        #return {"name":self.name, "price":self.price, "author":self.author}
        return f"Customers({"name":self.name, "price":self.price, "author":self.author}"")
