from db import db

class AccountableModel(db.Model):
    __tablename__ = 'accountable'

    registry_number = db.Column(db.Integer, primary_key=True, autoincrement=False)
    kinship_degree = db.Column(db.String)

    patient_acc_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    person_acc_id = db.Column(db.Integer, db.ForeignKey('person.id'),  unique=True)

    def __init__(self, registry_number, kinship_degree, patient_acc, person_acc):
        self.registry_number = registry_number 
        self.kinship_degree = kinship_degree
        self.patient_acc = patient_acc
        self.person_acc = person_acc


    def json(self):
        return {
                    'registry_number': self.registry_number ,'kinship_degree': self.kinship_degree
                }

    @classmethod
    def find_by_registry_number(cls, id):
        return cls.query.filter_by(id=cls.registry_number).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()