import views
from flask import Flask, render_template

application = Flask(__name__)

if __name__ == "__main__":
    application.run(host='0.0.0.0')


@application.route("/")
def index():
    return render_template('index.html')


@application.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html", error=error), 404


application.register_blueprint(views.gb)
