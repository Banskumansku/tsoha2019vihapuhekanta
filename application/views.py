from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user
from sqlalchemy import func

from application import app, db
from application.tweets.models import Tweet
from application.tweets.views import tweet_query_user
from application.votes.models import Vote
from application.votes.views import add_vote


@app.route("/")
@login_required
def index():
    tweet_query = tweet_query_user().all()
    normal = normal_size(tweet_query)
    offensive = offensive_size(tweet_query)
    hateful = hateful_size(tweet_query)
    random_tweet = randRow()
    vote = db.session.query().filter(Vote.tweet_id == random_tweet.id)
    return render_template("index.html", tweets=len(tweet_query), tweetsNormal=normal,
                           tweetsOffensive=offensive, tweetsHateful=hateful, tweet=random_tweet)


@app.route("/<id>", methods=['POST'])
def random_tweet_vote(id):
    tweet_id = id
    disposition = request.form.get("vote_button")
    add_vote(tweet_id, disposition)
    return redirect(url_for("index"))


def randRow():
    row_id = Tweet.query.order_by(func.random()).first().id
    row = Tweet.query.get(row_id)
    return row


def normal_size(tweetquery):
    return len(tweetquery)


def offensive_size(tweetquery):
    return len(tweetquery)


def hateful_size(tweetquery):
    return len(tweetquery)
