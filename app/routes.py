from flask import render_template
from app import app
from app.forms import DogBreedForm

@app.route('/')
@app.route('/index')
def index(): #makes the dogbreedform the welcome page
    form = DogBreedForm()
    return render_template('breedform.html', title = 'Dog Info', form=form)
    