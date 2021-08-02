from flask import Flask, render_template
import requests

app = Flask(__name__)
response = requests.get('https://api.npoint.io/ed99320662742443cc5b')
ALL_POSTS = response.json()

@app.route('/')
def home():
    return render_template("index.html", all_posts=ALL_POSTS)


@app.route('/blog/<int:num>')
def get_blog(num):
    blog = ALL_POSTS[num-1]
    # print(blog)
    return render_template("post.html", blog=blog)


if __name__ == "__main__":
    app.run(debug=True)
