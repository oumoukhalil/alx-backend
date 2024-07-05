#!/usr/bin/env python3
"""basic babel"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask('__name__')
babel = Babel(app)


class Config:
    """ config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LACALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@babel.localeselector
def get_local():
    """get user locale"""
    getlocal = request.args.get('locale')

    if getlocal in app.config['LANGUAGES']:
        return getlocal
    
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
   """root
   """
   return render_template('4-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
