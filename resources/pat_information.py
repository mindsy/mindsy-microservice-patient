#-*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, request
from flask_jwt_extended import jwt_required

from models.patiente import PatientModel 
from models.person import PersonModel
from models.telephone import TelephoneModel
from models.accountable import AccountableModel
from models.pat_psycho_hosp import Pat_Psycho_HospModel
from models.psychologist_hospital import PsychologistHospitalModel

class ShowInformationUserID(Resource):

    def get(self, id):
        person = PersonModel.find_by_id(id)
        if person:
            person_info = person.json()
            kinship = person.accountables.kinship_degree
            registry_number_acc = person.accountables.registry_number_acc
            registry_number_pat = person.patients.registry_number_pat
            date_of_birth = person.patients.dt_birth
            scholarit = person.patients.scholarit
            observation = person.patients.observation
            manual_domain = person.patients.manual_domain

            output = {'Basic Informations': [person_info], 'Accountables Informations': {'kinship_degree': kinship,'registry_number': registry_number_acc},
            'Patients Informations': {'registry_number': registry_number_pat, 'scholarit': scholarit, 'date of birth': date_of_birth,
            'observation': observation, 'manual_domain': manual_domain}}

            return {'Show Information': output}
        return {'message': 'User not found.'}, 404