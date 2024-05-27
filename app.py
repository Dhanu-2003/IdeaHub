from flask import Flask, render_template

app = Flask(__name__)

@app.route("/logout")
def logout():
    return "Logout"

@app.route("/aboutIdeaHub")
def aboutidea():
    return "aboutIdeaHub"

@app.route("/login")
def login():
    return "Login"

@app.route("/profile")
def profile():
    return "profile"

@app.route("/orders")
def orders():
    return "orders"

@app.route("/cart")
def cart():
    return "cart"

@app.route("/components")
def components():
    return "components"

@app.route("/signup")
def signup():
    return "signup"

@app.route("/details")
def details():
    return "details"

@app.route("/review")
def revies():
    return "review"

@app.route("/PlaceOrder")
def placeorder():
    return "PLACE ORDER"

@app.route("/product")
def product():
    return "product"

@app.route("/return")
def return_pro():
    return "return"

@app.route("/prototype")
def prototype():
    return "prototype"



if __name__=="__main__":
    app.run()
