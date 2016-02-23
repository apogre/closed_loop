from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    gamedatas = db.relationship('GameData', backref='user', lazy='dynamic')
    affectivs = db.relationship('Affectiv', backref='user', lazy='dynamic')

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, value):
        return check_password_hash(self.password, value)

    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active(self):
        return True

    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % self.username

class GameData(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    level = db.Column(db.Integer)
    score = db.Column(db.Integer)
    stack = db.Column(db.Integer)
    created = db.Column(db.DateTime)

    def __init__(self, level, score, stack, created):
        self.level = level
        self.score = score
        self.stack = stack
        self.created = created

    def __repr__(self):
        return '<GameData %r>' % self.gamedata

class Affectiv(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    engagement = db.Column(db.Float)
    excitementlongterm = db.Column(db.Float)
    excitementshorterm = db.Column(db.Float)
    frustration = db.Column(db.Float)
    meditation = db.Column(db.Float)
    created = db.Column(db.DateTime)

    def __init__(self, engagement, excitementlongterm, excitementshorterm, frustration,meditation, created):
        self.engagement = engagement
        self.excitementlongterm = excitementlongterm
        self.excitementshorterm = excitementshorterm
        self.frustration = frustration
        self.meditation = meditation
        self.created = created

    def __repr__(self):
        return '<Affectiv %r>' % self.affectiv