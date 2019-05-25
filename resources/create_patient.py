# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse

from datetime import datetime

from static.imports import *


class RegisterPatient(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('status',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('number',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('telephone_type',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('date_of_birth',
                        type=lambda d: datetime.strptime(d, '%d-%m-%Y')
                        )
    parser.add_argument('kinship_degree',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('scholarity',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('observation',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('manual_domain',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('registry_number_pat',
                        type=str,
                        required=False
                        )
    parser.add_argument('registry_number_acc',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('id_psychologist_hospital',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = RegisterPatient.parser.parse_args()

        if PersonModel.find_by_email(data['email']):
            return {"message": "A user with that email already exists"}, 400

        if TelephoneModel.find_by_number(data['number']):
            return {"message": "A user with that number already exists"}, 400

        if PatientModel.find_by_registry_number_pat(data['registry_number_pat']) and \
                data['registry_number_pat'] is not None:
            return {"message": "A user with that registry number patient already exists"}, 400

        if AccountableModel.find_by_registry_number_acc(data['registry_number_acc']):
            return {"message": "A user with that registry number accountable already exists"}, 400

        if len(data['number']) > 15 or len(data['number']) < 8 or not data['number'].isdigit():
            return {"message": "Type a valid telephone_number"}

        if str(data['telephone_type'].lower()) != str("residencial") and str(data['telephone_type'].lower()) != str(
                "pessoal") \
                and str(data['telephone_type'].lower()) != str("comercial"):
            return {"message": "Type a valid telephone_type"}

        if str(data['status'].lower()) != str("andamento") and str(data['status'].lower()) != str(
                "aguardando") \
                and str(data['status'].lower()) != str("finalizado"):
            return {"message": "Type a valid status"}

        if str(data['manual_domain'].lower()) != str("destro") and str(data['manual_domain'].lower()) != str(
                "canhoto"):
            return {"message": "Type a valid manual_domain"}

        if len(data['name']) <= 1:
            return {"message": "Type a valid name"}

        new_person = PersonModel(data['name'], data['email'])
        new_person.save_to_db()

        new_telephone = TelephoneModel(data['number'], data['telephone_type'], new_person.id)
        new_telephone.save_to_db()

        new_accountable = AccountableModel(data['registry_number_acc'], data['kinship_degree'], new_person.id)
        new_accountable.save_to_db()

        new_patient = PatientModel(data['scholarity'], data['observation'],
                                   data['manual_domain'], data['registry_number_pat'], data['date_of_birth'],
                                   new_person.id, new_accountable.registry_number_acc, data['status'])
        new_patient.save_to_db()

        new_pat_psycho_hosp = PatPsychoHospModel(data['id_psychologist_hospital'], new_patient.id_patient)
        new_pat_psycho_hosp.save_to_db()

        return {"message": "User created successfully.", "id_patient": new_patient.id_patient}, 201
