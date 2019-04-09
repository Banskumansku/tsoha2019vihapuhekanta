from flask_login import login_required, current_user

from application import app, db, api, errors
from flask import redirect, render_template, request, url_for

from application.logs.views import add_log
from application.tweets.models import Tweet
from application.tweets.forms import TweetForm, TweetSearchForm
from application.votes.views import delete_vote


@app.route("/tweets", methods=['GET', 'POST'])
@login_required
def tweets_index():
    search = TweetSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    tweets = tweet_query_user().all()
    return render_template("tweets/list.html", tweets=tweets, form=search)


@app.route("/tweets/results")
@login_required
def search_results(search):
    searchResults = []
    searchString = search.data['search']

    if searchString:
        if search.data['select'] == 'Tweet Text':
            searchQuery = db.session().query(Tweet).filter(Tweet.tweettext.contains(searchString),
                                                           (Tweet.account_id == current_user.id))
            searchResults = searchQuery.all()
        elif search.data['select'] == 'Tweet Type':
            searchQuery = db.session().query(Tweet).filter(Tweet.tweettype.contains(searchString),
                                                           (Tweet.account_id == current_user.id))
            searchResults = searchQuery.all()
        return render_template("tweets/list.html", tweets=searchResults, form=search)
    elif searchString == "":
        searchResults = db.session().query(Tweet).filter(Tweet.account_id == current_user.id)
        return render_template("tweets/list.html", tweets=searchResults, form=search)


@app.route("/tweets/new/")
@login_required
def tweets_form():
    return render_template("tweets/new.html", form=TweetForm())


@app.route("/tweets/<id>")
@login_required
def tweets_view(id):
    tweets = db.session().query(Tweet).filter(Tweet.id == id)
    return render_template('tweets/tweet.html', tweets=tweets)


@app.route("/tweets/<id>", methods=["POST"])
@login_required
def tweet_edit(id):
    tweet = db.session().query(Tweet).filter(Tweet.id == id).first()
    tweet.tweetdescription = request.form.get("tweetdescription")
    db.session().commit()
    add_log("edit", current_user.id, id)
    return redirect(url_for("tweets_index"))


@app.route("/tweets/<id>/delete", methods=["POST"])
@login_required
def tweet_delete(id):
    delete_vote(id)
    db.session.delete(Tweet.query.filter_by(id=id).first())
    db.session.commit()
    add_log("delete", current_user.id, id)
    return redirect(url_for("tweets_index"))


@app.route("/tweets/", methods=["POST"])
@login_required
def tweets_create():
    form = TweetForm(request.form)
    if not form.validate():
        return render_template("tweets/new.html", form=form)
    try:
        text = api.get_status(form.tweetid)
    except errors as e:
        return render_template("tweets/new.html", texterror=e[0], form=form)
    else:
        t = Tweet(form.tweetid.data, form.tweettype.data, form.tweetdescription.data, current_user.name)
        t.account_id = current_user.id
        t.addedby = current_user.name
        t.tweettext = text.text
        db.session().add(t)
        db.session().commit()
        add_log("create", current_user.id, t.id)
        return redirect(url_for("tweets_index"))


def tweet_query_user():
    return db.session().query(Tweet).filter(Tweet.account_id == current_user.id)
