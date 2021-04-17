'''
This program helps you to render HTML template in flask.We are creating a form in html and we are processing the entered values
You should create an HTML file inside a folder called "templates"
in the same directory
'''
from flask import Flask #import the Flask object from the flask package
from flask import render_template#for rendering html page
from flask import redirect,url_for#for redirecting to another webpage
from flask import request#for accessing data from form
app=Flask(__name__)#creating your Flask application instance with the name app

@app.route("/")#pass '/' to signify that this function respond to main URL
def home():
    return "HELLO"#connects with html page
@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":#when the method is post(while entering data from keyboard) we are storing the input value in to variable user and calls user function
        user=request.form["nm"]
        return redirect(url_for("user",usr=user))
    else:
        return render_template("index2.html")#if method is post(while clicking submit button) we have to be in the same page
@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"#printing value

if __name__=="__main__":
   app.run()#run the development server.