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



@app.route('/breeds')
def getbreeds():
    breeds = db.session.query(DogBreeds).all()
    return jsonify(DogBreedWeight=[i.serialize for i in breeds])

@app.route ('/singlebreed/<int:post_id>')
def getbreed(post_id):
        breeds = db.session.query(DogBreeds).all()
        Dogs = [i.serialize for i in breeds]
        for row in Dogs:
            if row['breedid'] == post_id:
                return jsonify(results=row)

@app.route ('/breeds', methods = ['POST'])
def new_breed():
    if not request.json:
        return "please enter in json"
    else:
        print('nothing')
    breeds = db.session.query(DogBreeds).all()
    Dogs = [i.serialize for i in breeds]
    newbreed = DogBreeds(breedid=Dogs[-1]['breedid'] + 1, breedname=request.json['breedname'], minweight=request.json['minweight'], maxweight=request.json['maxweight'])
    db.session.add(newbreed)
    db.session.commit()
    return '', 204

@app.route('breeds/<int:put_id>', methods=['PUT'])
def update_breed(put_id):
    breeds = db.session.query(DogBreeds).all()
    Dogs = [i.serialize for i in breeds]
    for row in Dogs:
        if row['breedid'] == put_id:
            DogBreeds(breedid=['put_id'], breedname=request.json['breedname'], minweight=request.json['minweight'], maxweight=request.json['maxweight'])
    return '',204


#@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
#def delete_task(task_id):
 #   task = [task for task in tasks if task['id'] == task_id]
  #  if len(task) == 0:
   #     abort(404)
    #tasks.remove(task[0])
#    return jsonify({'result': True})