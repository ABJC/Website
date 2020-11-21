from flask import Flask, g



# def create_app(test_config=None):
app = Flask(__name__, instance_relative_config=True)

# apply the blueprints to the app
from app.blueprints import beta

app.register_blueprint(beta.bp, url_prefix="/<locale>/beta")

# g.localization = "DE"
# Error Handlers
# app.register_error_handler(404, page_not_found)
# app.register_error_handler(500, page_not_found)

app.add_url_rule("/", endpoint="beta.index")
