from app import db

class Entry(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    tweet = db.Column(db.String(1000), nullable=False)
    url = db.Column(db.String(500))
    sarcasm = db.Column(db.Boolean)
    relevant = db.Column(db.Boolean, default=False)
    sentiment = db.Column(db.Integer, default=False)

    def __repr__(self):
        return self.tweet
