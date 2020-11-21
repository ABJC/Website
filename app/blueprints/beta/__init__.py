from flask import Blueprint

from flask import render_template, request, current_app, redirect, url_for
from flask import abort

from app import utils
from app.blueprints.beta.forms import *

bp = Blueprint("beta", __name__, url_prefix="/")


@bp.route("/")
def index(**options):
    locale, strings = utils.localization(options.get('locale', 'en'), 'beta')
    return render_template("beta/index.html", locale=locale, strings=strings)


@bp.route("/join")
def join(**options):
    locale, strings = utils.localization(options.get('locale', 'en'), 'beta')

    if request.method == 'POST':
        print(request.form)
        # flash('Thanks for registering')
        return redirect(url_for('beta.thanks'))
    return render_template("beta/join.html", locale=locale, strings=strings)


@bp.route("/thanks")
def thanks(**options):
    return "Thanks"