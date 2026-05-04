import os
import secrets
from flask import current_app

# def save_media(form_media, folder):
#     random_hex = secrets.token_hex(8)
#     _, f_ext = os.path.splitext(form_media.filename)
#     media_fn = random_hex + f_ext
#     # folder will be 'post_pics' or 'post_videos'
#     media_path = os.path.join(current_app.root_path, 'post', 'static', folder, media_fn)
    
#     form_media.save(media_path)
#     return media_fn


import os
import secrets
from flask import current_app

def save_media(form_media, folder_name):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_media.filename)
    media_fn = random_hex + f_ext
    
    # We are inside 'theblog', but we need to go into the 'post' folder first
    # then 'static', then your specific media folder.
    static_path = os.path.join(current_app.root_path, 'post', 'static', folder_name)
    
    # Auto-create the folder if it doesn't exist
    if not os.path.exists(static_path):
        os.makedirs(static_path)
        
    media_path = os.path.join(static_path, media_fn)
    form_media.save(media_path)

    return media_fn