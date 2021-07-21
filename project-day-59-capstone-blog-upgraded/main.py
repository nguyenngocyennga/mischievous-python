from flask import Flask, render_template
import requests

app = Flask(__name__)
response = requests.get("https://api.npoint.io/e42b353ee387383898c7")
ALL_POSTS = response.json()


@app.route('/')
@app.route('/index')
def home():
    return render_template("index.html", posts=ALL_POSTS)


@app.route('/blog/<int:num>')
def post(num):
    blog = ALL_POSTS[num-1]
    return render_template("post.html", blog=blog)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

