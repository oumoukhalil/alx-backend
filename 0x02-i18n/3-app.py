from flask import Flask, request, render_template
from flask_babel import Babel, _

app = Flask('__name__')
app.url_map.strict_slashes = False
babel = Babel(app)

class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    return render_template('3-index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
