from flask import render_template, request, Blueprint
from flaskapp import db
# from flaskapp.models import User
# from flaskapp.posts.forms import UserForm

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')

@main.route("/about")
def about():
    return render_template('about.html', title='about')