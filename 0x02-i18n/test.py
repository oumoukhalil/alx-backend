from flask import Flask, render_template
from flask_babel import Babel, format_datetime, gettext
from datetime import datetime

app = Flask(__name__)
babel = Babel(app)

# Configuration et initialisation de Flask-Babel
class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "ar"
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@app.route('/')
def test_flask_babel():
    # Utilisation de la fonction gettext pour traduire un message
    greeting = gettext('Hello, World!')

    # Formatage d'une date en utilisant Flask-Babel
    formatted_datetime = format_datetime(datetime(1987, 3, 5, 17, 12))

    return render_template('test.html', greeting=greeting, formatted_datetime=formatted_datetime)

if __name__ == "__main__":
    app.run()
