#EXPLANATION FOR THIS CODE IS PRESENT IN VIDEO2 (  https://www.youtube.com/watch?v=xIgPMguqyws&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX&index=2   )
'''
->Run the application.Then open a browser and type in the URL http://127.0.0.1:5000/   ,
    you will receive the string HELLO as a response, this confirms
    that your application is successfully running.
->The website will also display your HELLO [your name] when you type it in URL(http://127.0.0.1:5000/name)
->When you enter admin in URL it the page will redirect to page which prints HELLO [admin!] (http://127.0.0.1:5000/admin)
'''
from flask import Flask #import the Flask object from the flask package
from flask import redirect,url_for#for redirecting to another webpage
app=Flask(__name__)#creating your Flask application instance with the name app

@app.route("/")#pass '/' to signify that this function respond to main URL
def home():
    return "HELLO"#returns string "HELLO"
@app.route("/admin")#when parameter is admin control goes here
def admin():
    return redirect(url_for("user",name="admin!"))#control goes to user function.We are passing the value for name from here
@app.route("/<name>")#passing parametrs
def user(name):
    return f"HELLO {name}"#returns string "HELLO"
if __name__=="__main__":
   app.run()#run the development server