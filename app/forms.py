from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.fields.html5 import TelField
from wtforms.validators import DataRequired, length
from app.models import City

class MessageForm(FlaskForm):
    author = StringField('Имя:', validators=[DataRequired()])
    phone = StringField('Номер телефона:', validators=[DataRequired()])
    city = SelectField('Город', validators=[DataRequired()], choices=[
        (record.id, record.name) for record in City.query.all()
    ])
    body = TextAreaField('Сообщение', validators=[DataRequired()])
    submit = SubmitField('Отправить')
    # Валидность номера телефона
