from app import app, db
import csv
import flask
from flask import json, jsonify

from app.models import DogBreeds


@app.route('/')
@app.route('/index')
def index():
    message = {"hello": "world"}
    return flask.jsonify(message)


@app.route('/load')
def load_resources():
    with open('app/dogweight.csv', 'rt') as dogweightcsv:  # open csv
        reader = csv.reader(dogweightcsv, delimiter=",")  # load each row as an instance (dataitem) of dogbreedclass
        print(reader)
        next(reader, None)  # skip the headers
        for row in reader:
            data = DogBreeds(breedid=row[0], breedname=row[1], minweight=row[2], maxweight=row[3])
            db.session.add(data)
        return "Resources loaded.  There are now %i resources into the database." % db.session.query(DogBreeds).count()
        db.session.commit()


@app.route('/get')
def getbreeds():
    with open('app/dogweight.csv', 'rt') as dogweightcsv:  # open csv
        reader = csv.reader(dogweightcsv, delimiter=",")  # load each row as an instance (dataitem) of dogbreedclass
        print(reader)
        next(reader, None)  # skip the headers
        for row in reader:
            data = DogBreeds(breedid=row[0], breedname=row[1], minweight=row[2], maxweight=row[3])
            db.session.add(data)
            breeds = db.session.query(DogBreeds).all()
        return jsonify(DogBreedWeight=[i.serialize for i in breeds])

@app.route ('/getbreed/<int:post_id>')
def getbreed(post_id):
    with open('app/dogweight.csv', 'rt') as dogweightcsv:  # open csv
        reader = csv.reader(dogweightcsv, delimiter=",")  # load each row as an instance (dataitem) of dogbreedclass
        print(reader)
        next(reader, None)  # skip the headers
        breeds = db.session.query(DogBreeds).all()
        jsonify(DogBreedWeight=[i.serialize for i in breeds])
        if 'breedid' == post_id :
            return 



