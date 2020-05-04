from flask import render_template,url_for,redirect,Blueprint

welcome = Blueprint('welcome',__name__)

@welcome.route('/welcome')
def welcomebase():
    return render_template("welcome.html")