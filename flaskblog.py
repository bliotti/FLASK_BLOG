from flask import Flask, render_template, url_for
app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)