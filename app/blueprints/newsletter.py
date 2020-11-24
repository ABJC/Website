from flask import Blueprint

from flask import render_template, request, current_app, redirect, url_for, flash
from flask import abort

from app import utils
from app.mailchimp import Mailchimp
from app.connect import ConnectAPI

bp = Blueprint("newsletter", __name__, url_prefix="/")


@bp.route("/")
def index(**options):
    locale, strings = utils.localization(options.get('locale', 'en'))

    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')

        success_newsletter = Mailchimp().addSubscriber(email, fname, lname)

        if not (success_newsletter):
            # flash(strings['error'])
            print("ERROR")
            # TODO

    return render_template("newsletter/index.html", locale=locale, strings=strings)


@bp.route("/thanks/<name>")
def thanks(name: str, **options):
    locale, strings = utils.localization(options.get('locale', 'en'))
    return render_template("newsletter/thanks.html", locale=locale, strings=strings, name=name)
