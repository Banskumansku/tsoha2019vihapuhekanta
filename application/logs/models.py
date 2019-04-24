from application import db


class Log(db.Model):
    __tablename__ = "logs"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modification = db.Column(db.String(144), nullable=False)
    account_id = db.Column(db.Integer, nullable=False)
    tweet_id = db.Column(db.Integer, nullable=True)

    def __init__(self, modification, account_id, tweet_id):
        self.modification = modification
        self.account_id = account_id
        self.tweet_id = tweet_id

    def get_id(self):
        return self.id
