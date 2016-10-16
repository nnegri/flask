from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application-form")
def application_form():
    """Provides an application form to the user to submit."""

    return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def submit_application():
    """Submits application."""

    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    if request.form.get("jobtitle") == "software-engineer":
        jobtitle = "Software Engineer"
    elif request.form.get("jobtitle") == "qa-engineer":
        jobtitle = "QA Engineer"
    else:
        jobtitle = "Product Manager"

    #jobtitle = request.form.get("jobtitle")

    return render_template("application-response.html", firstname=firstname, 
                            lastname=lastname, jobtitle=jobtitle)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

