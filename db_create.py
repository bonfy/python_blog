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

db.session.add(User("test", "test@test.com", "i'll-never-tell"))
db.session.add(User("admin", "ad@min.com", "admin"))
db.session.add(User("test2", "test2@test3.com", "tell"))

db.session.add(Post("Good", "I\'m good.",1))
db.session.add(Post("Well", "I\'m well.",1))
db.session.add(Post("Excellent", "I\'m excellent.",2))
db.session.add(Post("Okay", "I\'m okay.",2))
db.session.add(Post("postgres", "we setup a local postgres instance",3))
db.session.add(Post("markdown", '''
# Markdown

----

Markdown is a text formatting syntax inspired on plain text email. In the words of its creator, [John Gruber][]:

[John Gruber]: http://daringfireball.net/


### Links

Inline links:

```
[link text](http://url.com/ "title")
[link text](http://url.com/)
## Syntax Guide

### Strong and Emphasize

```
*emphasize*    **strong**
_emphasize_    __strong__
```

**Shortcuts**

- Add/remove bold:
    Command-B for Mac / Ctrl-B for Windows and Linux

''', 3))

db.session.add(Post("markdown", unicode('中文'), 3))

# commit the changes
db.session.commit()
