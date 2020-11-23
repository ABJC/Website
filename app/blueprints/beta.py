from flask import Blueprint

from flask import render_template, request, current_app, redirect, url_for, flash
from flask import abort

from app import utils
from app.mailchimp import Mailchimp
from app.connect import ConnectAPI

bp = Blueprint("beta", __name__, url_prefix="/")


@bp.route("/")
def index(**options):
    locale, strings = utils.localization(options.get('locale', 'en'))
    return render_template("beta/index.html", locale=locale, strings=strings)


@bp.route("/join", methods=('GET', 'POST'))
def join(**options):
    locale, strings = utils.localization(options.get('locale', 'en'))

    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        newsletter = request.form.get('newsletter')
        success_newsletter = True
        if newsletter:
            success_newsletter = Mailchimp().addSubscriber(email, fname, lname)
        
        success_testflight = ConnectAPI().invite_tester(email, fname, lname)

        if not (success_testflight or success_newsletter):
            # flash(strings['error'])
            print("ERROR")
            # TODO

        return redirect(url_for('beta.thanks', name=fname if fname != None else "", locale=locale))

    return render_template("beta/join.html", strings=strings)


@bp.route("/thanks/<name>")
def thanks(name: str, **options):
    locale, strings = utils.localization(options.get('locale', 'en'))
    return render_template("beta/thanks.html", locale=locale, strings=strings, name=name)
