#!/usr/bin/env python3

"""babel basics"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask("__name__")
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    """get user locale"""
    getlocale = request.args.get('locale')

    if getlocale in app.config['LANGUAGES']:
        return getlocale
    
    return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_user():
    """user loggin"""
    user_id = request.args.get("login_as")
    if user_id:
        return users.get(int(user_id))
    return None

@app.before_request
def before_request():
    """before request"""
    g.user = get_user()

@app.route('/')
def index():
    """root"""
    return render_template('5-index.html')

if __name__ == "__main__":
    """execute as main"""
    app.run(host="0.0.0.0", port=5000, debug=True)
