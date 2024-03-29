# Build API with RESTful Routing

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice
from distutils.util import strtobool

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # dictionary = {}
        # for column in self.__table__.columns:
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")
    

# HTTP GET - Read Record
@app.route('/random')
def show_random_cafe():
    all_cafes = Cafe.query.all()
    random_cafe = choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route('/all')
def show_all_cafes():
    cafes = Cafe.query.all()
    data = [cafe.to_dict() for cafe in cafes]
    return jsonify(cafe=data)


@app.route('/search')
def search_cafe():
    if "loc" in request.args:
        loc = request.args.get('loc')
        cafes = db.session.query(Cafe).filter_by(location=loc).all()
        if len(cafes) == 0:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})
        else:
            data = [cafe.to_dict() for cafe in cafes]
            return jsonify(cafe=data)
    else:
        return jsonify(error={"No Field": "No location field provided. Please specify the location."})


# HTTP POST - Create Record
@app.route('/add', methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        has_sockets=strtobool(request.form.get('has_sockets')),
        has_toilet=strtobool(request.form.get('has_toilet')),
        has_wifi=strtobool(request.form.get('has_wifi')),
        can_take_calls=strtobool(request.form.get('can_take_calls')),
        seats=request.form.get('seats'),
        coffee_price=request.form.get('coffee_price')
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route('/update_price/<int:cafe_id>', methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get('new_price')
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        # 200 = Ok
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        # 404 = Resource not found
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


# HTTP DELETE - Delete Record
@app.route('/report_close/<int:cafe_id>', methods=["DELETE"])
def report_close(cafe_id):
    api_key = request.args.get('api_key')
    if api_key != "TopSecretAPIKey":
        # 403 Forbidden
        return jsonify(error={"Not Valid Key": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403
    else:
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


if __name__ == '__main__':
    app.run(debug=True)
