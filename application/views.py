from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from application import app, db, api
from application.tweets.models import Tweet


@app.route("/")
@login_required
def index():
    tweetquery = db.session().query(Tweet).filter(Tweet.account_id.contains(current_user.id))
    tweetSize = tweetquery.all()
    tweetquery = db.session().query(Tweet).filter(Tweet.account_id.contains(current_user.id),
                                                  Tweet.tweettype.contains("normal"))
    normal_size = tweetquery.all()
    tweetquery = db.session().query(Tweet).filter(Tweet.account_id.contains(current_user.id),
                                                  Tweet.tweettype.contains("offensive"))
    offensive_size = tweetquery.all()
    tweetquery = db.session().query(Tweet).filter(Tweet.account_id.contains(current_user.id),
                                                  Tweet.tweettype.contains("hateful"))
    hateful_size = tweetquery.all()
    return render_template("index.html", tweets=len(tweetSize), tweetsNormal=len(normal_size),
                           tweetsOffensive=len(offensive_size), tweetsHateful=len(hateful_size))
