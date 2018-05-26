from flask import render_template
from app import app
from app.forms import DogBreedForm
import csv

@app.route('/')
@app.route('/index')
def index(): 
    return "Welcome!"
#@app.route('/load')
#def load(): #loads data
    # def load_resources(self):
    #   with open('dogweight.csv', 'rb') as dogweightcsv: #open csv
     #      reader = csv.reader(dogweightcsv, delimiter=csv.excel.delimiter, quotechar=csv.excel.quotechar)    #load each row as an instance (dataitem) of dogbreedclass
      #     next(reader, None)  # skip the headers
       #    for row in reader:
        #       data = Muttweight(id=row[0], breed=row[1], minweight=row[2], maxweight=row[3])
         #      db.session.add(resource)
          # print("Resources loaded.  There are now %i resources into the database." % db.session.query(ThrivResource).count())
       #db.session.commit()
    
#def getbreeds():
#    for line in db:
        
        
