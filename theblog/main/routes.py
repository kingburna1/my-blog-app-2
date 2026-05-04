from flask import Blueprint, render_template
from flask_login import login_required, current_user
from theblog import db
from theblog.models import Post

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
@main.route('/home')
@login_required
def home(): 
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return  render_template('home.html', posts=posts)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact')
@login_required
def contact():
    return render_template('contact.html')

