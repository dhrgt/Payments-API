from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app) #indicate to Flask that this is a REST API app
db = SQLAlchemy() #instantiate database

class CustomerModel(db.Model): #create database model for customers object
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=True)

    def __init__(self, name, address, phone, email, description):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.description = description

    def json(self):
        return {"name":self.name, "address":self.address, "phone":self.phone, "email":self.email, "description":self.description}

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

class Customers(Resource):
    def get(self):
        result = CustomerModel.query.all()
        return {'result':list(x.json() for x in result)}

    def post(self):
        data = request.get_json(force=True)
        new_customer = CustomerModel(data['name'], data['address'], data['phone'],data['email'],data['description'])
        db.session.add(new_customer)
        db.session.commit()
        return new_customer.json(), 201 #201 means created

api.add_resource(Customers, '/customer')

#run app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
