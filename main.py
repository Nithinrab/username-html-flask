from flask import Flask, render_template

new = Flask(__name__)


@new.route("/login")
def user():
    return render_template("login.html")

@new.route("/register")
def reg():
    return render_template("register.html")

if __name__=="__main__":
    new.run()