from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask.ext.login import login_user, logout_user, login_required

from pixelracer.extensions import cache
from pixelracer.forms import LoginForm
from pixelracer.models import User, GameData, db
from datetime import datetime

main = Blueprint('main', __name__)
speed = 70

@main.route('/')
@cache.cached(timeout=1000)
def home():
    return render_template('game.html', speed_car=40)

@main.route('/tetris')
@cache.cached(timeout=1000)
def tetris():
    return render_template('tetris.html')

@main.route('/get_speed')
def speed_val():
	# a = open("speed_val", "rb")
	return str(speed)

@main.route('/send_score/<score>')
def send_score(score):
	global speed
	if (int(score) >= 5):
		speed = speed+10
		return "changed"
	elif (int(score)<=-5):
		speed = speed - 10
		return "changed"
	else:
		speed=speed
		return "done"

@main.route('/send_tetris_score', methods=['GET'])
def send_tetris_score():
    username = request.args.get('user')
    level =  request.args.get('level')
    score = request.args.get('score')
    stack = 5
    created = datetime.now()
    db.session.add(GameData(level, score, stack, created))
    db.session.commit()
    return "done"

@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one()
        login_user(user)

        flash("Logged in successfully.", "success")
        return redirect(request.args.get("next") or url_for(".home"))

    return render_template("login.html", form=form)


@main.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out.", "success")

    return redirect(url_for(".home"))


@main.route("/restricted")
@login_required
def restricted():
    return "You can only see this if you are logged in!", 200
