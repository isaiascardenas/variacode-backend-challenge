from flask import Blueprint

welcome_blueprint = Blueprint("welcome", __name__)


@welcome_blueprint.route("/")
def index():
    return """
        <html><body>
        <h2>Welcome!</h2>
        <p>To PagerDuty Customer Success Group Innovation Team
Back End Take Home Exercise, developed by isaiascardenas</p>
<div><p>Please checkout README.md for the API usage</p></div>
        </body></html>
    """
