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

    return '<h1>Hello {}</h1> <p>Shoe: {}</p><p>Bike: {}</p>'.format(
            athlete.firstname, athlete.shoes[0].name, athlete.bikes[0].name
            )

@app.route('/login')
def login():
    client = stravalib.client.Client()
    auth_url = client.authorization_url(client_id=CLIENT_ID,
            scope='write',
            redirect_uri='http://127.0.0.1:7123/auth')
    return '<a href="{}">Authenticate with Strava</a>'.format(auth_url)

@app.route('/auth')
def auth_done():
    # TODO: check for errors 
    code = flask.request.args.get('code', '')
    client = stravalib.client.Client()
    token = client.exchange_code_for_token(client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            code = code)
    flask.session['access_token'] = token
    print "Got token {}".format(token)
    return flask.redirect(flask.url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=7123)
