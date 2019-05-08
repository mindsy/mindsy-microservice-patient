from db import db


class Pat_Psycho_HospModel(db.Model):
    __tablename__ = 'pat_psycho_hosp'

    id_pat_psycho_hosp = db.Column(db.Integer, primary_key=True)

    psychologist_hospital_pat_psycho_hosp_id = db.Column(db.String, db.ForeignKey('psychologist_hospital.id_psycho_hosp'))
    patient_pat_psycho_hosp_id = db.Column(db.Integer, db.ForeignKey('patient.id_patient'))


    def __init__(self, psychologist_hospital, patient_pat_psycho_hosp):
        self.psychologist_hospital_pat_psycho_hosp = psychologist_hospital
        self.patient_pat_psycho_hosp = patient_pat_psycho_hosp


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()