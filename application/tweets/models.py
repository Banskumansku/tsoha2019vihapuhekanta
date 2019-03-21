
from application import db

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())
    tweetid = db.Column(db.String(100))
    tweettype = db.Column(db.String(100))
    tweettext = db.Column(db.String(300))
    addedby = db.Column(db.String(100))
    tweetdescription = db.Column(db.String(100))


    def __init__(self, tweetid, tweettype, tweetdescription):
        self.tweetid = tweetid
        self.tweettype = tweettype
        self.tweetdescription = tweetdescription
        self.addedby = "admin"
        self.tweettext = "lorem"

