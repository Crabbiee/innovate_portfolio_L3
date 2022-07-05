from flask import Flask, render_template, Blueprint, redirect, url_for

my_view = Blueprint('my_view', __name__)

@my_view.route('/')
def index():
    return render_template("index.html")

@my_view.route('/abbie')
def abbie():
    return render_template("abbie.html")

@my_view.route('/about')
def about():
    return render_template("about.html")
# # # # # # # ^ THESE POINT TO PAGES ^ # # # # #

@my_view.route('/aboutme')
def about_redirect():
    return redirect(url_for("my_view.about"))
# # # # # # REDIRECTS ^ # # # # # # 