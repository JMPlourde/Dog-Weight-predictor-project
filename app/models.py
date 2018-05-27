from app import db


class DogBreeds(db.Model):
    __tablename__='DogBreeds'
    id = db.Column(db.Integer, primary_key = True)
    breedname = db.Column(db.String, index = True, unique = True)
    minweight = db.Column(db.Integer, index=True, unique = False)
    maxweight = db.Column(db.Integer, index = True, unique = False)

def __repr__(self):
    return '<DogBreeds {}>'.format(self.breedname)

db.create_all()
db.session.commit()