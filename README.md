strava-fixer
============

Strava Fixer fixes your data on strava.com

The first feature it will support is adding gear - bike or
shoes - to activities that lack any data. This is useful
if you have imported a large amount of historical data into
Strava and wish to add your gear to it.

It is licenced under the AGPL 3.0.

Joel Stanley <joel@jms.id.au>
September 2014

Installation
------------
Strava Fixer is written in Python 2. The requirements.txt
file lists the Python dependencies.

```
$ virtualenv .
$ . bin/activate
$ pip install -r requirements.txt
```

A configuration file is required

```
$ cat settings.txt << EOF
SECRET_KEY = 'generate a random string here'
CLIENT_SECRET = '41 character Strava API client secret'
CLIENT_ID = 'Strava API client ID'
EOF

$ export FIXSTRAVA_CONFIG=settings.txt
$ python app.py
```
