#-*- coding: utf-8 -*-
from flask_restful import Resource

from static.imports import *
from db import db


class ShowAllInformationPatient(Resource):
    def get(self, crp):

        if PsychologistModel.find_by_crp(crp):
            
            persons = (db.session.query(PersonModel, PatientModel, PsychologistModel, PatPsychoHospModel, HospitalModel,
                                        PsychologistHospitalModel)
            .filter(PsychologistModel.crp == crp)
            .filter(HospitalModel.registry_number == '4002')
            .filter(PsychologistModel.crp == PsychologistHospitalModel.crp_psychologist_crp)
            .filter(HospitalModel.registry_number == PsychologistHospitalModel.hospital_registry_number)
            .filter(PatientModel.id_patient == PatPsychoHospModel.patient_hosp_psy_id_patient)
            .filter(PsychologistHospitalModel.id_psycho_hosp == PatPsychoHospModel.pat_psycho_hosp_id_psycho_hosp)
            .filter(PersonModel.id == PatientModel.person_pat_id) 
            .all())
            
            flag = 1
            number_persons = len(persons)
            output = []
            for person in persons:
                if flag <= number_persons:
                    output.append({'number_patient': flag})
                    flag += 1

                patient_info = {'person_informations': [person[0].json()],
                'patient_informations': [person[0].patients.json()],
                'accoutable_information': [person[0].patients.ACCOUNTABLE.json()]
                }
                
                output.append(patient_info)
            return {"Patient's Psychologists": output}, 200

        else:
            return {"message": "We could not localizated this crp"}, 400


class ShownPatientInformationID(Resource):
    def get(self, id):

        patient = PatientModel.find_by_id(id)
        if patient:
            person_info = patient.PERSON.json()
            acc_info = patient.ACCOUNTABLE.json()
            patient_info = patient.json()

            output = {'Basic Informations': [person_info],
                    'Accountables Information': [acc_info],
                    'Patients Information': [patient_info]}

            return {'Show Information': output}

        return {'message': 'User not found.'}, 404
