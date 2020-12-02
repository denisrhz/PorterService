from flask import render_template
from app import app
from app.forms import MessageForm
from app.models import Service

@app.route('/')
def index():
    services = Service.query.all()
    return render_template('index.html', services=services)

@app.route('/message/<service>', methods=['GET', 'POST'])
def message(service):
    form = MessageForm()
    # Доделать обработку формы
    return render_template('message.html', form=form, service=service)

