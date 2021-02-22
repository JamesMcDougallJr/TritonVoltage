import os
from flask import Flask, render_template
from .triton_voltage import voltage_reading

project_dir = os.path.dirname(os.path.abspath(__file__))

def create_app():
    # create and configure the app
    app = Flask(__name__)
    register_errorhandlers(app)
    return app

def register_errorhandlers(app):
    """Register error handlers."""
    @app.errorhandler(401)
    def internal_error(error):
        return render_template('401.html'), 401

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('500.html'), 500

    return None

app = create_app()

@app.route('/')
def root():
    return voltage_reading.reading()

