from theblog.models import Comment, Post, PostLike
from flask import Blueprint, render_template, url_for, flash, redirect, abort, request
from flask_login import current_user, login_required
from theblog import db
from theblog.post.utils import save_media
from theblog.post.forms import PostForm, DeletePostForm

posts = Blueprint('posts', __name__, template_folder='templates', static_folder='static', static_url_path='/posts/static')


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        # Initialize the post object first with text content
        post = Post(
            title=form.title.data, 
            content=form.content.data, 
            author=current_user
        )
        
        # Only update the image_file attribute if a new image was uploaded
        if form.image_file.data:
            post.image_file = save_media(form.image_file.data, 'post_pics')
            
        # Only update the video_file attribute if a video was uploaded
        if form.video_file.data:
            post.video_file = save_media(form.video_file.data, 'post_videos')
            
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
        
    return render_template('create_post.html', title='New Post', legend='New Post', form=form)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    
    form = PostForm()
    
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        
       
        if form.image_file.data:
           
            picture_file = save_media(form.image_file.data, 'post_pics')
            post.image_file = picture_file
       
        if form.video_file.data:
            video_file = save_media(form.video_file.data, 'post_videos')
            post.video_file = video_file
            
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
        
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        
        
    return render_template("create_post.html", title='Update Post', 
                           legend='Update Post', form=form)
    
    
    
@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    form = DeletePostForm()
    comments = Comment.query.filter_by(post_id=post.id).all()   
    return render_template("post.html", 
                           title=post.title, 
                           post=post, 
                           form=form,
                           comments=comments)
    
    
@posts.route("/like_post/<int:post_id>", methods=['POST'])
@login_required
def like_post(post_id):
    post = Post.query.get_or_404(post_id)
    existing_like = PostLike.query.filter_by(post_id=post.id, user_id=current_user.id).first()
    if existing_like:
        db.session.delete(existing_like)
    else:
        db.session.add(PostLike(post_id=post.id, user_id=current_user.id))
    db.session.commit()
    return redirect(request.referrer) 

@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id): # <--- This name must match the endpoint
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))