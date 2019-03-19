from application import app, db
from flask import redirect, render_template, request, url_for
from application.tweets.models import Tweet


@app.route("/tweets", methods=["GET"])
def tweets_index():
    return render_template("tweets/list.html", tweets=Tweet.query.all())


@app.route("/tweets/new/")
def tweets_form():
    return render_template("tweets/new.html")

@app.route("/delete", methods=["POST"])
def delete():
    tweetid = request.form.get("tweetid")
    tweet = Tweet.query.filter_by(tweetid=tweetid).first()
    db.session.delete(tweet)
    db.session.commit()
    return redirect(url_for("tweets_index"))


@app.route("/tweets/", methods=["POST"])
def tweets_create():
    t = Tweet(request.form['tweetid'], request.form['tweettype'])
    print("asdasdasda")
    db.session().add(t)
    db.session().commit()
    return redirect(url_for("tweets_index"))