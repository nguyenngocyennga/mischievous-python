from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)


@app.route('/')
def guess():
    return "<b>Hi there, this is just the beginning!</b>" \
           "<p><i>Let's secretly pick a number between 0 and 9 *sshhh*</i></p>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></img>"


@app.route('/<int:number>')
def check_number(number):
    if number < random_number:
        return "<h1 style='color:red'><b>Too low, try again!</b></h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'></img>"
    elif number > random_number:
        return "<h1 style='color:red'><b>Too high, try again!</b></h1>" \
                   "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'></img>"
    else:
        return "<h1 style='color:green'><b>YAY! YOU GOT IT!</b></h1>" \
           "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'></img>"


if __name__ == "__main__":
    app.run(debug=True)
