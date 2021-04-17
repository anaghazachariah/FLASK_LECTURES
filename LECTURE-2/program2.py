'''
->This program helps you to render HTML template in flask.
->Flask program passes an argument to html page
You should create an HTML file inside a folder called "templates"
in the same directory
'''
from flask import Flask #import the Flask object from the flask package
from flask import render_template#for rendering html page
app=Flask(__name__)#creating your Flask application instance with the name app

@app.route("/<name>")#passing parametrs
def user(name):
    return render_template("index2.html",content=name)#connects with html page with argument name(it is possible to pass multiple arguments)
@app.route("/")#pass '/' to signify that this function respond to main URL
def home():
    return "HELLO"#returns string "HELLO"
if __name__=="__main__":
   app.run()#run the development server.