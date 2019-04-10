from werkzeug.security import generate_password_hash, check_password_hash

from application import db


class User(db.Model):
    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    urole = db.Column(db.String(80))
    tweets = db.relationship("Tweet", backref='account', lazy=True)

    def __init__(self, username, password, urole):
        self.name = username
        self.username = username
        self.password = password
        self.urole = urole

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        if (self.urole == "ADMIN"):
            return ["ADMIN"]
        else:
            return ["USER"]

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
