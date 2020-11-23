from flask import Blueprint

from flask import render_template, request, current_app, redirect, url_for, flash
from flask import abort

from app import utils

bp = Blueprint("changelog", __name__, url_prefix="/")


@bp.route("/")
def index(**options):
    locale, strings = utils.localization(options.get('locale', 'en'))
    versions = utils.get_data('changelog.json')
    return render_template("changelog.html", locale=locale, strings=strings, versions=versions)