from flask import Flask, request
from flask_restful import Api

app=Flask(__name__)



#run app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
