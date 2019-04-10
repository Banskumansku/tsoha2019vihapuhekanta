from sqlalchemy import text

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

    @staticmethod
    def find_users_least_voted_tweet(user_id):
        stmt = text("SELECT votes.tweet_id, votes.oppose, account.username, tweet.tweettext FROM votes"
                    " JOIN Tweet ON votes.tweet_id = tweet.id"
                    " JOIN account ON tweet.account_id = :user_id"
                    " WHERE tweet.account_id = :user_id"
                    " ORDER BY votes.oppose DESC"
                    ).params(user_id=user_id)
        res = db.engine.execute(stmt)

        response = []
        if res is None:
            return None

        for row in res:
            response.append({"oppose": row[1], "tweettext": row[3]})
            pass

        return response

    @staticmethod
    def find_users_most_voted_tweet(user_id):
        stmt = text("SELECT votes.tweet_id, votes.affirm, account.username, tweet.tweettext FROM votes"
                    " JOIN Tweet ON votes.tweet_id = tweet.id"
                    " JOIN account ON tweet.account_id = :user_id"
                    " WHERE tweet.account_id = :user_id"
                    " ORDER BY votes.affirm DESC"
                    ).params(user_id=user_id)
        res = db.engine.execute(stmt)

        response = []
        if res is None:
            return None

        for row in res:
            response.append({"affirm": row[1], "tweettext": row[3]})
            pass

        return response
