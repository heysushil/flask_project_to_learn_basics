from flask import Flask
from flask import url_for
from markupsafe import escape # script inject prevent using the mehtod

app = Flask(__name__) # created instance

# create as much as method whcih required and at first before each function create the routh or url of that funtion so that accesss on url

# its default method
@app.route('/')
def index():
    return 'Hello I am a Index or default method'

# created rout to run this method
@app.route("/login")
def login():
    return f'Login!'

# show the post with given id
@app.route("/user/<username>")
def show_post(username):
    return f'User {escape(username)}!'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('show_post', username='John'))

if __name__ == "__main__":
    app.run()
