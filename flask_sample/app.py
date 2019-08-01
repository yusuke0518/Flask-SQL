from flask import *
from .database import *
from .models.models import User,Order
import flask_sample.models


def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_sample.config.Config')

    init_db(app)

    return app

app = create_app()

@app.route("/",methods=["GET"])
def show():
    return render_template("hello.html")

@app.route("/user/register",methods=("GET","POST"))
def register_user():
    if request.method == "POST":
        user=User()
        user.name = request.form["name"]
        user.password = request.form["password"]
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("show"))
    else:
        return render_template("register_user.html")

@app.route("/user/list",methods=["GET"])
def show_users():
    users = User.query.all()
    return render_template("users.html",contents=users)

@app.route("/order/register",methods=("GET","POST"))
def register_order():
    if request.method == "POST":
        order=Order()
        order.name = request.form["name"]
        order.price = int(request.form["price"])
        order.kind = request.form["kind"]
        print(order.kind)
        order.feature = request.form["feature"]
        print(11)
        db.session.add(order)
        db.session.commit()
        print(11333)


        return redirect(url_for("show"))
    else:
        return render_template("register_order.html")

@app.route("/order/list",methods=["GET"])
def show_orders():
    orders = Order.query.all()
    return render_template("orders.html",contents=orders)