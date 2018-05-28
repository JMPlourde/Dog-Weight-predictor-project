from app import db


class DogBreeds(db.Model):
    __tablename__='DogBreeds'
    breedid = db.Column(db.Integer, primary_key = True)
    breedname = db.Column(db.String, index = True, unique = True)
    minweight = db.Column(db.Integer, index=True, unique = False)
    maxweight = db.Column(db.Integer, index = True, unique = False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.breedid,'breedname': self.breedname,'minweight': self.minweight,'maxweight': self.maxweight}

def __repr__(self):
    return '<DogBreeds {}>'.format(self.breedname)



db.create_all()
db.session.commit()