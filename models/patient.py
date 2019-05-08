from db import db


class PatientModel(db.Model):
    __tablename__ = 'patient'

    id_patient = db.Column(db.Integer, primary_key=True)
    scholarit = db.Column(db.String)
    observation = db.Column(db.String)
    manual_domain = db.Column(db.String)
    registry_number = db.Column(db.String)
    dt_birth = db.Column(db.String)


    person_pat_id = db.Column(db.Integer, db.ForeignKey('person.id'), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def json(self):
        return {'id': self.id ,'name': self.name, 'email': self.email, 'telephone': [telephone.json() for telephone in self.telephones.all()]}

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()