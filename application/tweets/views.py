from application import app, db
from flask import redirect, render_template, request, url_for
from application.tweets.models import Tweet
from application.tweets.forms import TweetForm, TweetSeachForm


@app.route("/tweets", methods=['GET', 'POST'])
def tweets_index():
    search = TweetSeachForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template("tweets/list.html", tweets=Tweet.query.all(), form=search)

@app.route("/tweets/results")
def search_results(search):
    searchResults = []
    searchString = search.data['search']

    if searchString:
        if search.data['select'] == 'Tweet Id':
            searchQuery = db.session().query(Tweet).filter(Tweet.tweetid.contains(searchString))
            searchResults = searchQuery.all()
        elif search.data['select'] == 'Tweet Type':
            searchQuery = db.session().query(Tweet).filter(Tweet.tweettype.contains(searchString))
            searchResults = searchQuery.all()
    if not searchResults:
        return redirect(url_for("tweets_index"))
    else:
        return render_template("tweets/list.html", tweets=searchResults, form=search)


@app.route("/tweets/new/")
def tweets_form():
    return render_template("tweets/new.html", form = TweetForm())

@app.route("/delete", methods=["POST"])
def delete():
    tweetid = request.form.get("tweetid")
    tweet = Tweet.query.filter_by(tweetid=tweetid).first()
    db.session.delete(tweet)
    db.session.commit()
    return redirect(url_for("tweets_index"))


@app.route("/tweets/", methods=["POST"])
def tweets_create():
    form = TweetForm(request.form)

#    if not form.validate():
 #       return render_template("tweets/new.html", form = form)

    t = Tweet(form.tweetid.data, form.tweettype.data, form.tweetdescription.data)
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tweets_index"))