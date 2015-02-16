from flask_wtf import Form
from wtforms import TextField, TextAreaField, DateField, SelectField
from wtforms.validators import optional, DataRequired, Length
from datetime import datetime


class MessageForm(Form):
    title = TextField('Title', validators=[DataRequired()])
    content = TextAreaField('Description', validators=[DataRequired()])
    tag_id = SelectField('Tag', coerce=int)
    insert_dt = DateField('Date', default=datetime.now(), validators=[optional()])


class TodoForm(Form):
    title = TextField('Title', validators=[DataRequired()])