#!/usr/bin/python

import flask
import logging
import stravalib

app = flask.Flask(__name__)
app.config.from_envvar('FIXSTRAVA_CONFIG')

logging.basicConfig(level=logging.INFO)

app.secret_key = SECRET_KEY

@app.route('/')
def homepage():
    if 'access_token' not in flask.session:
        return flask.redirect(flask.url_for('login'))

    client = stravalib.client.Client(access_token=flask.session['access_token'])
    athlete = client.get_athlete()

    return flask.render_template('main.html', athlete=athlete)

@app.route('/login')
def login():
    client = stravalib.client.Client()
    auth_url = client.authorization_url(client_id=CLIENT_ID,
            scope='write',
            redirect_uri='http://127.0.0.1:7123/auth')
    return flask.render_template('login.html', auth_url=auth_url)

@app.route('/logout')
def logout():
    flask.session.pop('access_token')
    return flask.redirect(flask.url_for('homepage'))

@app.route('/update')
def update():
    return flask.render_template('update.html')

@app.route('/auth')
def auth_done():
    # TODO: check for errors 
    code = flask.request.args.get('code', '')
    client = stravalib.client.Client()
    token = client.exchange_code_for_token(client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            code = code)
    flask.session['access_token'] = token
    return flask.redirect(flask.url_for('homepage'))

if __name__ == '__main__':
    app.run(debug=True, port=7123)
