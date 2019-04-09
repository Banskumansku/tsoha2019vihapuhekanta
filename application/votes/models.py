from application import db


class Vote(db.Model):
    __tablename__ = "votes"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    affirm = db.Column(db.Integer, nullable=True)
    oppose = db.Column(db.Integer, nullable=True)
    tweet_id = db.Column(db.Integer, nullable=False)

    def __init__(self, tweet_id):
        self.tweet_id = tweet_id

    def get_id(self):
        return self.id
