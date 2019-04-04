from flask import render_template

from application import app, db
from application.logs.models import Log


@app.route("/logs/list", methods=["GET"])
def view_logs():
    logs = db.session().query(Log).all()
    return render_template("logs/list.html", logs=logs)


def add_log(modification, tweet_id, account_id):
    if modification == "delete":
        m = "User deleted tweet"
        l = Log(m, account_id, tweet_id)
        db.session().add(l)
        db.session().commit()
    elif modification == "edit":
        m = "User edited tweet"
        l = Log(m, account_id, tweet_id)
        db.session().add(l)
        db.session().commit()

    elif modification == 'create':
        m = "User created tweet"
        l = Log(m, account_id, tweet_id)
        db.session().add(l)
        db.session().commit()

    elif modification == 'account_delete':
        m = "User account deleted"
        l = Log(m, account_id)
        db.session().add(l)
        db.session().commit()

    elif modification == 'account_created':
        m = "User account created"
        l = Log(m, account_id)
        db.session().add(l)
        db.session().commit()