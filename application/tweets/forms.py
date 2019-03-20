from flask_wtf import FlaskForm
from wtforms import Form, StringField, validators, SelectField

class TweetForm(FlaskForm):
    tweetid = StringField("Tweet Id")
    tweettext = StringField("Tweet Text")
    postedby = StringField("Posted By")
    choices = ['normal', 'offensive', 'hateful']
    tweettype = SelectField("Type of Text", choices)
    class Meta:
        csrf = False

class TweetSeachForm(Form):
    choices = [('Tweet Id', 'Tweet Id'), ('Tweet Type', 'Tweet Type')]
    select = SelectField('Search for tweets: ', choices=choices)
    search = StringField('')