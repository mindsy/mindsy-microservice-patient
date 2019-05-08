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

    def __init__(self, scholarit, observation, manual_domain, registry_number, dt_birth):
        self.scholarit = scholarit 
        self.observation = observation
        self.manual_domain = manual_domain
        self.registry_number = registry_number
        self.dt_birth = dt_birth

    def json(self):
        return {
                    'id': self.id_patient ,'scholarit': self.scholarit, 'observation': self.observation,
                    'manual_domain': self.manual_domain, 'registry number': self.registry_number, 
                    'date of birth': self.dt_birth
                }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=self.id_patient).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()