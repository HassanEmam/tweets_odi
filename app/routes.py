from flask import render_template, request, redirect
from app import app, db
from app.models import Entry

jedi = "of the jedi"


@app.route('/')
@app.route('/index')
def index():

    entry = Entry.query.filter_by(sentiment=None).first()
    entries = Entry.query.all()
    tweets_count = len(entries)
    labelled = Entry.query.filter(Entry.sentiment!=None).all()
    completed = len(labelled)
    remaining = len(entries) - len(labelled)
    print(tweets_count, len(labelled), remaining)
    #print(entry.tweet, entries)
    return render_template('index.html', entry=entry, entries=entries, completed=completed, remaining=remaining)


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        form = request.form
        tweet = form.get('tweet')
        sarcasm = (form.get('sarcasm')== '1')
        relevant = (form.get('relevant')=='1')
        sentiment = form.get('sentiment')
        id = form.get('tweet_id')
        print("form data", form, tweet, sarcasm, relevant)
        if tweet:
            entry = Entry.query.get(id)
            entry.sarcasm = sarcasm
            entry.sentiment = sentiment
            entry.relevant = relevant
            db.session.add(entry)
            db.session.commit()
            return redirect('/')

    return "of the jedi"


@app.route('/update/<int:id>')
def updateRoute(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            return render_template('update.html', entry=entry)

    return "of the jedi"


@app.route('/update', methods=['POST'])
def update():
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')

    return "of the jedi"


@app.route('/delete/<int:id>')
def delete(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')

    return "of the jedi"


@app.route('/turn/<int:id>')
def turn(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            entry.status = not entry.status
            db.session.commit()
        return redirect('/')

    return "of the jedi"

# @app.errorhandler(Exception)
# def error_page(e):
#     return "of the jedi"


