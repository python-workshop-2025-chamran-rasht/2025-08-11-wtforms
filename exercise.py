from flask import Flask, render_template, flash, redirect
from forms import LoginForm, SignupForm

app = Flask(__name__)

app.config.from_object('default_config')
app.config.from_prefixed_env()

# using this instead of a database
# is a terrible idea, but this is a simple exercise,
# so whatever...
USERS_DICTIONARY = {
    # 'username': 'password'
}

@app.route('/')
def index_ep():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login_ep():
    form = LoginForm()

    if form.validate_on_submit():
        flash('You are logged in.')
        return redirect('/')

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup_ep():
    # to use a global variable inside our function,
    # we need the "global" keyword
    global USERS_DICTIONARY
    form = SignupForm()

    if form.validate_on_submit():
        # your objectives:
        # check if username is duplicate
        # store username and password
        # show success message
        # redirect to login page
        raise NotImplemented("implement this block, and remove this line.")

    return render_template('signup.html', form=form)
