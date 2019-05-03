from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user
from sqlalchemy import func

from application import app
from application.tweets.models import Tweet
from application.tweets.views import tweet_query_user
from application.votes.models import Vote
from application.votes.views import add_vote


@app.route("/")
def index():
    if not current_user.is_authenticated:
        return render_template("index.html")

    most_votes = Vote.find_users_most_voted_tweet(current_user.id)
    least_votes = Vote.find_users_least_voted_tweet(current_user.id)
    try:
        most_positively_voted = most_votes[0]
        most_negatively_voted = least_votes[0]
    except Exception as e:
        most_positively_voted = None
        most_negatively_voted = None
        print(e)

    tweet_query = tweet_query_user()
    amounts = [0, 0, 0, 0]
    for row in tweet_query:
        print(row.tweettype)
        if row.tweettype == 'normal':
            amounts[0] = amounts[0] + 1
            amounts[1] = amounts[1] + 1
        elif row.tweettype == 'offensive':
            amounts[0] = amounts[0] = amounts[0] + 1
            amounts[2] = amounts[2] + 1
        else:
            amounts[0] = amounts[0] = amounts[0] + 1
            amounts[3] = amounts[3] + 1

    try:
        random_tweet = randRow()
    except Exception as e:
        random_tweet = None
        print(e)

    return render_template("index.html", all=amounts, tweet=random_tweet, most_positively_voted=most_positively_voted,
                           most_negatively_voted=most_negatively_voted)


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
