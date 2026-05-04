from flask import Blueprint
from flask_wtf import FlaskForm
from theblog.models import User
from flask_login import current_user
from wtforms import StringField,SubmitField,TextAreaField, FileField
from flask_wtf.file import FileAllowed
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    image_file = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    video_file = FileField('Upload Video', validators=[FileAllowed(['mp4', 'mov', 'avi'])])
    submit = SubmitField('Post')
    
    
class DeletePostForm(FlaskForm):
    submit = SubmitField('Delete')