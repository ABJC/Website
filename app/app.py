from flask import Flask, render_template, request
from datetime import datetime
from app import utils

def error_handler_404(error):
    locale, strings = utils.localization(request.path.split("/")[1])
    return render_template("errors.html", code="404", strings=strings), 404

def error_handler_500(error):
    locale, strings = utils.localization(request.path.split("/")[1])
    return render_template("errors.html", code="500", strings=strings), 500


# def create_app(test_config=None):
app = Flask(__name__, instance_relative_config=True)


# Apply the blueprints to the app
from app.blueprints import home, roadmap, changelog, beta, newsletter

app.register_blueprint(home.bp,     url_prefix="/")
app.register_blueprint(roadmap.bp,  url_prefix="/roadmap")
app.register_blueprint(changelog.bp,url_prefix="/changelog")
app.register_blueprint(beta.bp,     url_prefix="/beta")
app.register_blueprint(newsletter.bp, url_prefix="/newsletter")

app.register_blueprint(home.bp,     url_prefix="/<locale>/")
app.register_blueprint(roadmap.bp,  url_prefix="/<locale>/roadmap")
app.register_blueprint(changelog.bp,url_prefix="/<locale>/changelog")
app.register_blueprint(beta.bp,     url_prefix="/<locale>/beta")
app.register_blueprint(newsletter.bp,     url_prefix="/<locale>/newsletter")

app.register_blueprint(redirects.bp)
app.add_url_rule("/", endpoint="home.index")
app.register_error_handler(404, error_handler_404)


@app.template_filter()
def time_format(date_string: str):
    date = datetime.strptime(date_string, "%Y-%m-%d")
    return date.strftime("%B %d, %Y")

# @app.route("/robots.txt")
# def robots():
#     return "ROBOTS"


# g.localization = "DE"
# Error Handlers
# app.register_error_handler(404, page_not_found)
# app.register_error_handler(500, page_not_found)


