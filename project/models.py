# coding:utf-8

from project import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

import mistune


class Post(db.Model):

    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    content_html = db.Column(db.Text, nullable=False)
    insert_dt = db.Column(db.DateTime, default=str(datetime.utcnow())[:-7])

    # many to one  use backref
    author_id = db.Column(db.Integer, ForeignKey('user.id'))

    # many to one
    tag_id = db.Column(db.Integer, ForeignKey('tag.id'))
    tag = relationship("Tag")


    def __init__(self, title, content, author_id, insert_dt=None, tag_id=1):
        self.title = title
        self.content = content
        self.content_html = mistune.markdown(content)
        self.author_id = author_id

        if insert_dt:
            self.insert_dt = insert_dt

        self.tag_id = tag_id

    def __repr__(self):
        return '<title {}>'.format(self.title)


class User(db.Model):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100))
    insert_dt = db.Column(db.DateTime, default=str(datetime.utcnow())[:-7])
    post = relationship("Post", backref="author")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<name {}>'.format(self.name)


class Tag(db.Model):

    __tablename__ = "tag"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    insert_dt = db.Column(db.DateTime, default=str(datetime.utcnow())[:-7])

    def __init__(self, name):
        self.name = name


class Song(db.Model):

    __tablename__ = "song"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    insert_dt = db.Column(db.DateTime, default=str(datetime.utcnow())[:-7])

    def __init__(self, name, url):
        self.name = name
        self.url = url


class TodoList(db.Model):

    __tablename__ = 'todolist'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

    # 0 for 未完成， 1 for 完成
    flag = db.Column(db.Integer, default=0)
    insert_dt = db.Column(db.DateTime, default=str(datetime.utcnow())[:-7])
    finish_dt = db.Column(db.DateTime)


    def __init__(self, title):
        self.title = title

    def setFinished(self):
        self.flag = 1
        self.finish_dt = str(datetime.utcnow())[:-7]