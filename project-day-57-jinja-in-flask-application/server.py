from flask import Flask, render_template
import random
import requests
from datetime import date

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = date.today().year
    return render_template('index.html', num=random_number, year=year)


@app.route('/guess/<name>')
def guess_gender(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    gender = response.json()["gender"]
    return render_template('index.html', name=name.title(), gender=gender)


@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
