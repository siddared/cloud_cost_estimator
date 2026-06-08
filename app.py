from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from flask import url_for

from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from models import db
from models import User
from models import Estimate

from calculator import estimate_cost

from datetime import datetime

app = Flask(__name__)

app.config.from_pyfile("config.py")

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        existing_user = User.query.filter_by(
            username=username
        ).first()

        if existing_user:

            return render_template(
                "register.html",
                error="Username already exists!"
            )

        user = User(
            username=username,
            password=generate_password_hash(password)
        )

        db.session.add(user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = user.username
            return redirect("/dashboard")

        return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    return render_template("dashboard.html")


@app.route('/admin')
def admin():

    total_users = User.query.count()

    total_estimates = Estimate.query.count()

    estimates = Estimate.query.order_by(
        Estimate.id.desc()
    ).limit(10)

    return render_template(
        'admin.html',
        total_users=total_users,
        total_estimates=total_estimates,
        estimates=estimates
    )
@app.route(
    "/estimate",
    methods=["GET", "POST"]
)
def estimate():

    if request.method == "POST":

        region = request.form["region"]

        ec2_type = request.form["ec2"]

        ec2_hours = int(
            request.form["hours"]
        )

        s3_storage = float(
            request.form["storage"]
        )

        rds = int(
            request.form["rds"]
        )

        transfer = float(
            request.form["transfer"]
        )

        total = estimate_cost(
            ec2_type,
            ec2_hours,
            s3_storage,
            rds,
            transfer
        )

        record = Estimate(

            username=session.get("username", "Guest"),

            region=region,

            ec2_type=ec2_type,

            ec2_hours=ec2_hours,

            s3_storage=s3_storage,

            rds_instances=rds,

            data_transfer=transfer,

            total_cost=total,

            created_at=str(
                datetime.now()
            )
        )

        db.session.add(record)

        db.session.commit()

        return render_template(
            "estimate.html",
            total=total
        )

    return render_template(
        "estimate.html"
    )

@app.route('/report')
def report():

    return render_template(
        'report.html'
    )
@app.route("/history")
def history():

    data = Estimate.query.all()

    return render_template(
        "history.html",
        data=data
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )