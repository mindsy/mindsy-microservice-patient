from db import db


class PatientModel(db.Model):
    __tablename__ = 'patient'

    id_patient = db.Column(db.Integer, primary_key=True)
    scholarit = db.Column(db.String)
    observation = db.Column(db.String)
    manual_domain = db.Column(db.String)
    registry_number = db.Column(db.String)
    dt_birth = db.Column(db.String)

    # pat_psycho_hosps = db.relationship('Pat_Psycho_HospModel', backref='patient_pat_psycho_hosps', cascade='all, delete-orphan')

    person_pat_id = db.Column(db.Integer, db.ForeignKey('person.id'), unique=True)
    
    accountables = db.relationship('AccountableModel', backref='accountable_patient', cascade='all, delete-orphan')

    def __init__(self, scholarit, observation, manual_domain, registry_number, dt_birth, person_pat):
        self.scholarit = scholarit 
        self.observation = observation
        self.manual_domain = manual_domain
        self.registry_number = registry_number
        self.dt_birth = dt_birth
        self.person_pat = person_pat

    def json(self):
        return {
                    'id': self.id_patient ,'scholarit': self.scholarit, 'observation': self.observation,
                    'manual_domain': self.manual_domain, 'registry number': self.registry_number, 
                    'date of birth': self.dt_birth, 
                    'accontables': [accountable.json() for accountable in self.accountables.all()]
                }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=cls.id_patient).first()
    
    @classmethod
    def find_by_registry_number(cls, registry_number):
        return cls.query.filter_by(registry_number=cls.registry_number).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()