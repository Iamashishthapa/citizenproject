from flask import render_template,Blueprint

login = Blueprint('login', __name__)

@login.route('/login')
def loginbase():
    return render_template('login.html')