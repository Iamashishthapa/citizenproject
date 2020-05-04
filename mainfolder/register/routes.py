from flask import render_template,session,redirect,url_for,request,Blueprint

register = Blueprint('register',__name__)

@register.route('/register',methods=['GET', 'POST'])
def registerbase():
    if "user" in session:
        user = session["user"]
        return redirect(url_for("welcome",user=user))
    else:
        if request.method == "POST":
            user = request.form['suser']
            email =request.form['semail']
            password =request.form['spw']
            session["user"] = user
            # usr=User(user,email,password)
            # db.session.add(usr)
            # db.session.commit()
            return redirect(url_for("welcome",user=user))
        else:
            return render_template('register.html')