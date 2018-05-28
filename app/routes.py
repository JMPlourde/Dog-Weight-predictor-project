from app import app, db
import csv
import flask
from flask import json, jsonify, request

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
        db.session.commit()
        return "Resources loaded.  There are now %i resources into the database." % db.session.query(DogBreeds).count()



@app.route('/get')
def getbreeds():
    breeds = db.session.query(DogBreeds).all()
    return jsonify(DogBreedWeight=[i.serialize for i in breeds])

@app.route ('/getbreed/<int:post_id>')
def getbreed(post_id):
        breeds = db.session.query(DogBreeds).all()
        Dogs = [i.serialize for i in breeds]
        for row in Dogs:
            if row['breedid'] == post_id:
                return jsonify(results=row)

@app.route ('/post')
def new_breed():
    if not request.json or not 'title' in request.json:
        return "please enter in json"
    breeds = db.session.query(DogBreeds).all()
    newbreed = {
        'breedid': DogBreeds[-1]['id'] + 1,
        'breedname': request.json['title'],
        'minweight': request.json['minweight'],
        'maxweight': request.json['maxweight']
    }
    breeds.append(newbreed)
    return jsonify({'newbreed':newbreed})