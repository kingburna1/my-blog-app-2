from flask import Blueprint
main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    return "Welcome to the Blog Home Page!"

@main.route('/about')
def about():
    return "This is the About Page of the Blog."

@main.route('/contact')
def contact():
    return "This is the Contact Page of the Blog."

