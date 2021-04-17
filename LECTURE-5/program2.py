'''
#USE SAME INDEX AND BASE FILES OF PREVIOUS EXAMPLE
This program helps you to render HTML template in flask.We are creating a form in html and we are processing the entered values
You should create an HTML file inside a folder called "templates"
in the same directory
'''
from flask import Flask #import the Flask object from the flask package
from flask import render_template#for rendering html page
from flask import redirect,url_for#for redirecting to another webpage
from flask import request#for accessing data from form
from flask import session#for accessing session
from datetime import timedelta#accesing time
app=Flask(__name__)#creating your Flask application instance with the name app
app.secret_key="hello"
app.permanent_session_lifetime=timedelta(days=5)#here we are giving the session time as 5 days..we can also gives minutes instead of days
@app.route("/")#pass '/' to signify that this function respond to main URL
def home():
    return "HELLO"#connects with html page
@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":#when the method is post(while entering data from keyboard) we are storing the input value in to variable user and calls user function
        session.permanent=True#making the session permanent(ususally session is default)
        user=request.form["nm"]
        session["user"]=user#storing value in session
        return redirect(url_for("user"))
    else:
        if "user" in session:#if user is loged in even if we write user and login we will get user page
            return redirect(url_for("user"))
        return render_template("index1.html")#if method is post(while clicking submit button) we have to be in the same page
@app.route("/user")
def user():#user() function will get data from session
    if "user" in session:#we are checking whether the session is active or not
        user=session["user"]
        return f"<h1>{user}</h1>"#printing value
    else:
        return redirect(url_for("login"))#if session is not active we are going back to login page
@app.route("/logout")
def logout():#logout code
    session.pop("user",None)
    return redirect(url_for("login"))
if __name__=="__main__":
   app.run()#run the development server.