from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import MessageForm
from app.models import Service, Message

@app.route('/')
def index():
    services = Service.query.all()
    return render_template('index.html', services=services)

@app.route('/message/<service>', methods=['GET', 'POST'])
def message(service):
    form = MessageForm()
    if form.validate_on_submit():
        message = Message(author=form.author.data,
                            phone=form.phone.data,
                            body=form.body.data,
                            service_id=service,
                            city_id=form.city.data)
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('message', service=service))
    return render_template('message.html', form=form)

