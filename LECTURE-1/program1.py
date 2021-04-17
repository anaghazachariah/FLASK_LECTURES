'''
In this program program we are creating a simple webpage,which displays "HELLO"

Run the application.Then open a browser and type in the URL http://127.0.0.1:5000/   ,
you will receive the string HELLO as a response, this confirms
that your application is successfully running.
'''
from flask import Flask #import the Flask object from the flask package
app=Flask(__name__)#creating your Flask application instance with the name app

@app.route("/")#pass '/' to signify that this function respond to main URL
def home():
    return "HELLO"#returns string "HELLO"
if __name__=="__main__":
   app.run()#run the development server.