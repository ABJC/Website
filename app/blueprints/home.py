from flask import Blueprint

from flask import render_template, request, current_app, redirect, url_for, flash
from flask import abort

from app import utils

bp = Blueprint("home", __name__, url_prefix="/")


@bp.route("/")
def index(**options):
    locale, strings = utils.localization(options.get('locale', 'en'))
    return render_template("home.html", locale=locale, strings=strings)

@bp.route("/imprint")
def imprint(**options):
    locale, strings = utils.localization(options.get('locale', 'en'))
    return render_template("imprint.html", locale=locale, strings=strings)

@bp.route("/privacy")
def privacy(**options):
    locale, strings = utils.localization(options.get('locale', 'en'))
    return render_template("privacy.html", locale=locale, strings=strings)

@bp.route("/about")
def about(**options):
    locale, strings = utils.localization(options.get('locale', 'en'))
    return render_template("about.html", locale=locale, strings=strings)