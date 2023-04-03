from flask import Flask
from markupsafe import escape # script inject prevent using the mehtod

app = Flask(__name__) # created instance

# create as much as method whcih required and at first before each function create the routh or url of that funtion so that accesss on url

# its default method
@app.route('/')
def index():
    return 'Hello I am a Index or default method'

# created rout to run this method
@app.route("/user/<name>")
def show_user_profile(name):
    return f'Hello, {escape(name)}!'
    # return "<p>Hello World!</p>"

# show the post with given id
@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f'Post {post_id}!'

# show subpath after /path
@app.route('/path/<path:subpath>')
def subpath(subpath):
    return f'Subpath, {escape(subpath)}!'
