from flask import Flask, render_template, request
import requests
from account_info import my_email, my_password, recipient
import smtplib


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


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data['name'], data['email'], data['phone'], data['message'])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=recipient,
                            msg=f"Subject: New message on your blog"
                                f"\n\n{name}\n{email}\n{phone}\n{message}")


if __name__ == "__main__":
    app.run(debug=True)
