# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, request
from flask_jwt_extended import jwt_required

from models.patiente import PatientModel 
from models.person import PersonModel
from models.telephone import TelephoneModel
from models.accountable import AccountableModel
from models.pat_psycho_hosp import Pat_Psycho_HospModel
from models.psychologist_hospital import PsychologistHospitalModel

class EditPatient(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('email',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('number',
                        type=int,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('scholarity',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )

    parser.add_argument('observation',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('manual_domain',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )

    parser.add_argument('registry_number_pat',
                        type=str,
                        required=False
                        )
    parser.add_argument('dt_birth',
                        type=str,
                        required=False
                        )

    def put(self, id):
        data = Edit.parser.parse_args()

        person = PersonModel.find_by_id(id)

        if person:
            if data['name']:
                person.name = data['name']
            if data['email']:
                person.email = data['email']
            if data['number']:
                person.telephones[0].number = data['number']
            if data['scholarity']:
                person.patients.scholarity = data['scholarity']
            if data['observation']:
                person.patients.observation = data['observation']
            if data['manual_domain']:
                person.patients.manual_domain = data['manual_domain']
            if data['registry_number_pat']:
                person.patients.registry_number_pat = data['registry_number_pat']
            if data['dt_birth']:
                person.patient_dt_birth = data['dt_birth']

        else:
            return {'message': 'User not found.'}, 404

        person.save_to_db()

        return person.json()