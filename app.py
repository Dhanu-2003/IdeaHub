from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    product = [
        {"S_NO": 1, "COMPONENT": "Component 1", "COST": 100, "COUNT": 2, "TOTAL": 200},
        {"S_NO": 2, "COMPONENT": "Component 2", "COST": 150, "COUNT": 1, "TOTAL": 150},
        {"S_NO": 3, "COMPONENT": "Component 3", "COST": 200, "COUNT": 3, "TOTAL": 600},
        
    ]
    return render_template('product.html', products=product)


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
    product = [
        {"S_NO": 1, "COMPONENT": "Component 1", "COST": 100, "COUNT": 2, "TOTAL": 200},
        {"S_NO": 2, "COMPONENT": "Component 2", "COST": 150, "COUNT": 1, "TOTAL": 150},
        {"S_NO": 3, "COMPONENT": "Component 3", "COST": 200, "COUNT": 3, "TOTAL": 600}
    ]
    return render_template('product.html', products=product)
    

@app.route("/return")
def return_pro():
    return "return"

@app.route("/prototype")
def prototype():
    return "prototype"



if __name__=="__main__":
    app.run()
