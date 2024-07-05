#!/usr/bin/env python3

"""flask babel"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone
import pytz


app = Flask("__name__")
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config:
    """Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

@babel.localeselector
def get_locale():
    """Get locale
    """
    getlocale = request.args.get('locale')

    if getlocale in app.config['LANGUAGES']:
        return getlocale
    
    if g.user:
        getlocale = g.user.get('locale')
        if getlocale and getlocale in app.config['LANGUAGES']:
            return getlocale
        
    getlocale = request.headers.get('locale', None)
    if getlocale in app.config['LANGUAGES']:
        return getlocale
    
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@babel.timezoneselector
def get_timezone():
    """setup the timezone
    """
    tzone = request.args.get('timezone', None)
    if tzone:
        try:
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    
    if g.user:
        try:
            tzone = g.user.get('timezone')
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    default = app.config['BABEL_DEFAULT_TIMEZONE']

    return default

def get_user():
    """logggin fonction
    """
    user_id = request.args.get("login_as")
    if user_id:
        return users.get(int(user_id))
    return None

@app.before_request
def before_request():
    g.user = get_user()

@app.route('/')
def index():
    """the root
    """
    return render_template('7-index.html')


if __name__ == "__main__":
    """execute the program as main"""
    app.run(host="0.0.0.0", port=5000, debug=True)
