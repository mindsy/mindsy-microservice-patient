#-*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, request
from flask_jwt_extended import jwt_required
from models.psychologist import PsychologistModel
from models.patient import PatientModel
from models.pat_psycho_hosp import Pat_Psycho_HospModel 
from models.psychologist_hospital import PsychologistHospitalModel
from models.person import PersonModel
from models.hospital import HospitalModel
from db import db


class ShowAllInformationPatient(Resource):
    @jwt_required
    def get(self, crp):

        if PsychologistModel.find_by_crp(crp):
            
            persons = (db.session.query(PersonModel, PatientModel, PsychologistModel, Pat_Psycho_HospModel, HospitalModel, PsychologistHospitalModel )
            .filter(PsychologistModel.crp == crp)
            .filter(HospitalModel.registry_number == '4002')
            .filter(PsychologistModel.crp == PsychologistHospitalModel.crp_psychologist_crp)
            .filter(HospitalModel.registry_number == PsychologistHospitalModel.hospital_registry_number)
            .filter(PatientModel.id_patient == Pat_Psycho_HospModel.patient_hosp_psy_id_patient)
            .filter(PsychologistHospitalModel.id_psycho_hosp == Pat_Psycho_HospModel.pat_psycho_hosp_id_psycho_hosp)
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
                'accoutable_information': [person[0].patients.accountables.json()]
                }
                
                output.append(patient_info)
            return {"Patient's Psychologists": output}, 200

        else:
            return {"message": "We could not localizated this crp"}, 400
    
class ShownPatientInformationID(Resource):
    @jwt_required
    def get(self, id):
        try:
            patient = PatientModel.find_by_id(id)
            if patient:
                person_info = patient.person_pat.json()
                acc_info = patient.accountables.json()
                patient_info = patient.json()

                output = {'Basic Informations': [person_info],
                        'Accountables Informations': [acc_info],
                        'Patients Informations': [patient_info]}

                return {'Show Information': output}
        except:
            return {"Something wrong happened": output}, 500

        return {'message': 'User not found.'}, 404
