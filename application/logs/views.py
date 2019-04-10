from flask import render_template

from application import app, db, login_required
from application.logs.models import Log


@app.route("/logs/list", methods=["GET"])
@login_required(role="ADMIN")
def view_logs():
    logs = db.session().query(Log).all()
    return render_template("logs/list.html", logs=logs)


def add_log(modification, tweet_id, account_id):
    if modification == "delete":
        m = "User deleted tweet"
    elif modification == "edit":
        m = "User edited tweet"
    elif modification == 'create':
        m = "User created tweet"
    elif modification == 'account_delete':
        m = "User account deleted"
    elif modification == 'account_created':
        m = "User account created"
    elif modification == 'vote':
        m = "User voted on tweet"

    l = Log(m, account_id, tweet_id)
    db.session().add(l)
    db.session().commit()
