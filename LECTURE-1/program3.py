'''
->Run the application.Then open a browser and type in the URL http://127.0.0.1:5000/   ,
    you will receive the string HELLO as a response, this confirms
    that your application is successfully running.
->The website will also display your HELLO [your name] when you type it in URL(http://127.0.0.1:5000/name)
->When you enter admin in URL it the page will redirect to home page(http://127.0.0.1:5000/admin)
'''
from flask import Flask #import the Flask object from the flask package
from flask import redirect,url_for#for redirecting to another webpage
app=Flask(__name__)#creating your Flask application instance with the name app

@app.route("/")#pass '/' to signify that this function respond to main URL
def home():
    return "HELLO"#returns string "HELLO"
@app.route("/admin")#when parameter is admin control goes here
def admin():
    return redirect(url_for("home"))#control goes to home page
@app.route("/<name>")#passing parametrs
def user(name):
    return f"HELLO {name}"#returns string "HELLO"
if __name__=="__main__":
   app.run()#run the development server.