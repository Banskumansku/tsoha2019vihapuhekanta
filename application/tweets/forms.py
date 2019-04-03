from flask_wtf import FlaskForm
from wtforms import Form, StringField, validators, SelectField, IntegerField


class TweetForm(FlaskForm):
    id = StringField("Id")
    tweetid = StringField("Tweet Id", [validators.Length(19)])
    tweettext = StringField("Tweet Text")
    postedby = StringField("Posted By")
    tweettype = StringField("Type of Text")
    tweetdescription = StringField("Description", [validators.Length(max=256)])
    class Meta:
        csrf = False



class TweetSeachForm(Form):
    choices = [('Tweet Id', 'Tweet Id'), ('Tweet Type', 'Tweet Type')]
    select = SelectField('Search for tweets: ', choices=choices)
    search = StringField('')