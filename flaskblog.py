from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '7443020c844bdca9a819bff92ba31228'

posts = [
    {
        'author': "Brian Liotti",
        'title': "Blog 1",
        "content": "First Post content",
        "date_posted": "April 20th, 2018"
    },
    {
        'author': "Jane Doe",
        'title': "Blog 2",
        "content": "Second Post content",
        "date_posted": "April 28th, 2018"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
