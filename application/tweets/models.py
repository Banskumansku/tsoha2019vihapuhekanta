
from application import db

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    tweetid = db.Column(db.String(144), nullable=False)
    tweettype = db.Column(db.String(144), nullable=False)
    tweettext = db.Column(db.String(256), nullable=False)
    addedby = db.Column(db.String(144), nullable=False)

    def __init__(self, tweetid, tweettype):
        print("this is " + tweetid + " and " + tweettype)
        self.tweetid = tweetid
        self.tweettype = tweettype
        self.addedby = "admin"
        self.tweettext = "lorem"

