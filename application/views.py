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
    tweet_query = tweet_query_user()
    amounts = tweet_amounts(tweet_query.all())
    random_tweet = randRow()
    return render_template("index.html", all=amounts[1], tweetsNormal=amounts[2],
                           tweetsOffensive=amounts[3], tweetsHateful=amounts[4], tweet=random_tweet)


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


def tweet_amounts(tweet_query):
    amounts = [0, 0, 0, 0, 0]
    amounts[1] = 1
    amounts[2] = 0
    amounts[3] = 0
    amounts[4] = 0

    for row in tweet_query:
        if row.tweettype == "normal":
            amounts[0] = + 1
            amounts[1] = + 1
        elif row.tweettype == "offensive":
            amounts[0] = + 1
            amounts[2] = + 1
        else:
            amounts[0] = + 1
            amounts[3] = + 1
    return amounts
