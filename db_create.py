# coding:utf-8

from project import db
from project.models import Post,User,Tag,Song

# create the database and the db table
db.drop_all()
db.create_all()

# insert data

db.session.add(Tag(u'随便说说'))
db.session.add(Tag(u'Python'))
db.session.add(Tag(u'手机IOS'))
db.session.add(Tag(u'厨艺荟萃'))
db.session.add(Tag(u'旅游摄影'))

# commit the changes
db.session.commit()
