from flask import Blueprint

from flask import render_template, request, current_app, redirect, url_for, flash
from flask import abort

from app import utils

bp = Blueprint("roadmap", __name__, url_prefix="/")


@bp.route("/")
def index(**options):
    locale, strings = utils.localization(options.get('locale', 'en'))
    html = utils.get_data("roadmap.html")
    return render_template("roadmap.html", locale=locale, strings=strings)