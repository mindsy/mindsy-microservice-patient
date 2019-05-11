#-*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, request
from models.person import PersonModel


class ShowAllInformationPatient(Resource):
    def get(self):
        persons = PersonModel.query.all()
        output = []
        try:
            for person in persons:
                person_data = {}
                person_data['id_person'] = person.id
                person_data['name'] = person.name
                person_data['email'] = person.email
                person_data['number'] = person.telephones[0].number
                person_data['telephone_type'] = person.telephones[0].telephone_type
                person_data['id_patient'] = person.patients.id_patient
                person_data['scholarity'] = person.patients.scholarity
                person_data['observation'] = person.patients.observation
                person_data['date of birth'] = person.patients.dt_birth
                person_data['manual_domain'] = person.patients.manual_domain
                person_data['registry_number_pat'] = person.patients.registry_number_pat
                person_data['registry_number_acc'] = person.accountables.registry_number_acc
                person_data['kinship_degree'] = person.accountables.kinship_degree
                output.append(person_data)
        except:
            return {"Something wrong happened": output}, 500

        return {"Patients": output}, 200


class ShownPatientInformationID(Resource):
    def get(self, id):
        person = PersonModel.find_by_id(id)
        if person:
            person_info = person.json()
            kinship = person.accountables.kinship_degree
            registry_number_acc = person.accountables.registry_number_acc
            registry_number_pat = person.patients.registry_number_pat
            date_of_birth = person.patients.dt_birth
            scholarity = person.patients.scholarity
            observation = person.patients.observation
            manual_domain = person.patients.manual_domain

            output = {'Basic Informations': [person_info],
                      'Accountables Informations': {'kinship_degree': kinship, 'registry_number': registry_number_acc},
                      'Patients Informations': {'registry_number': registry_number_pat, 'scholarity': scholarity,
                                                'date of birth': date_of_birth,
                                                'observation': observation, 'manual_domain': manual_domain}}

            return {'Show Information': output}
        return {'message': 'User not found.'}, 404


