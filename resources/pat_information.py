#-*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, request
from models.patient import PatientModel


class ShowAllInformationPatient(Resource):
    def get(self):
        persons = PatientModel.query.all()
        output = []
        try:
            for patient in persons:
                person_data = {}
                person_data['id_person'] = patient.person_pat.id
                person_data['name'] = patient.person_pat.name
                person_data['email'] = patient.person_pat.email
                person_data['number'] = patient.person_pat.telephones[0].number
                person_data['telephone_type'] = patient.person_pat.telephones[0].telephone_type
                person_data['id_patient'] = patient.id_patient
                person_data['scholarity'] = patient.scholarity
                person_data['observation'] = patient.observation
                person_data['date of birth'] = patient.dt_birth
                person_data['manual_domain'] = patient.manual_domain
                person_data['registry_number_pat'] = patient.registry_number_pat
                person_data['registry_number_acc'] = patient.accountables.registry_number_acc
                person_data['kinship_degree'] = patient.accountables.kinship_degree
                output.append(person_data)
        except:
            return {"Something wrong happened": output}, 500

        return {"Patients": output}, 200


class ShownPatientInformationID(Resource):
    def get(self, id):
        patient = PatientModel.find_by_id(id)
        if patient:
            person_info = patient.json()
            kinship = patient.accountables.kinship_degree
            registry_number_acc = patient.accountables.registry_number_acc
            patient_info = patient.json()

            output = {'Basic Informations': [person_info],
                      'Accountables Informations': {'kinship_degree': kinship, 'registry_number': registry_number_acc},
                      'Patients Informations': [patient_info]}

            return {'Show Information': output}
        return {'message': 'User not found.'}, 404
