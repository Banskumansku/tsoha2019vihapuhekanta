from flask_wtf import FlaskForm
from wtforms import Form, StringField, validators, SelectField

class TweetForm(FlaskForm):
    id = StringField("Id")
    tweetid = StringField("Tweet Id")
    tweettext = StringField("Tweet Text")
    postedby = StringField("Posted By")
    tweettype = StringField("Type of Text")
    tweetdescription = StringField("Description")
    class Meta:
        csrf = False

class TweetSeachForm(Form):
    choices = [('Tweet Id', 'Tweet Id'), ('Tweet Type', 'Tweet Type')]
    select = SelectField('Search for tweets: ', choices=choices)
    search = StringField('')