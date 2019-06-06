#-*- coding: utf-8 -*-
from flask_restful import Resource

from static.imports import *
from db import db


class ShowAllInformationPatient(Resource):
    def get(self, crp):

        if PsychologistModel.find_by_crp(crp):
            
            persons = (db.session.query(PersonModel)
            .filter(PsychologistModel.crp == crp)
            .filter(HospitalModel.registry_number == '4002')
            .filter(PsychologistModel.crp == PsychologistHospitalModel.crp_psychologist_crp)
            .filter(HospitalModel.registry_number == PsychologistHospitalModel.hospital_registry_number)
            .filter(PatientModel.id_patient == PatPsychoHospModel.patient_hosp_psy_id_patient)
            .filter(PsychologistHospitalModel.id_psycho_hosp == PatPsychoHospModel.pat_psycho_hosp_id_psycho_hosp)
            .filter(PersonModel.id == PatientModel.person_pat_id) 
            .all())
            
            output = []
            for person in persons:
                person_info = person.json()
                patient_info = person.patients.json()
                person_info.update(patient_info)
                accountable_info = person.patients.ACCOUNTABLE.json()
                person_info.update(accountable_info)

                output.append(person_info)
            return {"Patient's Psychologists": output}, 200

        else:
            return {"message": "We could not localised this crp"}, 400


class ShownPatientInformationID(Resource):
    def get(self, id):

        patient = PatientModel.find_by_id(id)
        if patient:
            person_info = patient.PERSON.json()
            patient_info = patient.json()
            person_info.update(patient_info)
            acc_info = patient.ACCOUNTABLE.json()
            person_info.update(acc_info)

            return person_info

        return {'message': 'User not found.'}, 404
