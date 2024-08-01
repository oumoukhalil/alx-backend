#!/usr/bin/env python3

"""flask babel basic"""

from flask import Flask, request, render_template
from flask_babel import Babel


app = Flask('__name__')
babel = Babel(app)

class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LANGUAGE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    """get locale
    """
    return request.accept_languages.best_match(app.conf['LANGUAGES'])

@app.route('/')
def index():
    """root
    """
    return render_template('2-index.html')

if __name__ == "__main__":
    """execute as main"""
    app.run(host="0.0.0.0", port=5000, debug=True)
