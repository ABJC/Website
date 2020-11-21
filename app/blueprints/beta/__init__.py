from flask import Blueprint

from flask import render_template, request, current_app, redirect, url_for, flash
from flask import abort

from app import utils
from app.mailchimp import Mailchimp
from app.blueprints.beta.forms import *

bp = Blueprint("beta", __name__, url_prefix="/")


@bp.route("/")
def index(**options):
    locale, strings = utils.localization(options.get('locale', 'en'), 'beta.index')
    return render_template("beta/index.html", locale=locale, strings=strings)


@bp.route("/join", methods=('GET', 'POST'))
def join(**options):
    locale, strings = utils.localization(options.get('locale', 'en'), 'beta.join')

    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        mail = request.form.get('email')
        success = Mailchimp().addSubscriber(fname, lname, mail)
        if not success:
            # flash(strings['error'])
            print("ERROR")
        return redirect(url_for('beta.thanks', name=fname, locale=locale))

    return render_template("beta/join.html", strings=strings)


@bp.route("/thanks/<name>")
def thanks(name: str, **options):
    locale, strings = utils.localization(options.get('locale', 'en'), 'beta.thanks')
    return render_template("beta/thanks.html", locale=locale, strings=strings, name=name)
