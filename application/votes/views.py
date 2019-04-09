from flask_login import current_user

from application import db
from application.logs.views import add_log
from application.votes.models import Vote


def add_vote(tweet_id, disposition):
    vote = db.session().query(Vote).filter(Vote.tweet_id == tweet_id).first()

    if vote is None:
        vote = new_vote(tweet_id)

    if disposition == "Yes":
        vote.affirm = vote.affirm + 1
    else:
        vote.oppose = vote.oppose + 1

    db.session().commit()
    add_log("vote", tweet_id, current_user.id)


def new_vote(tweet_id):
    vote = Vote(tweet_id)
    vote.affirm = 0
    vote.oppose = 0
    db.session().add(vote)
    db.session().commit()
    return vote


def delete_vote(id):
    vote = db.session().query(Vote).filter(Vote.tweet_id == id).first()
    if vote is None:
        return
    db.session.delete(Vote.query.filter(Vote.tweet_id == id).first())
    db.commit()
