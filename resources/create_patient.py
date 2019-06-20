# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse
from datetime import datetime
from static.imports import *
from db import db


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
    parser.add_argument('crp',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = RegisterPatient.parser.parse_args()

        if PersonModel.find_by_email(data['email']):
            return {"message": "A user with that email already exists"}, 422

        if TelephoneModel.find_by_number(data['number']):
            return {"message": "A user with that number already exists"}, 422

        if PatientModel.find_by_registry_number_pat(data['registry_number_pat']) and \
                data['registry_number_pat'] is not None:
            return {"message": "A user with that registry number patient already exists"}, 422

        if AccountableModel.find_by_registry_number_acc(data['registry_number_acc']):
            return {"message": "A user with that registry number accountable already exists"}, 422

        if not PsychologistModel.find_by_crp(data['crp']):
            return {"message": "We could not found the crp"}, 404

        psycho_hosp = (db.session.query(PsychologistHospitalModel)
                          .filter(HospitalModel.registry_number == "4002")
                          .filter(PsychologistModel.crp == data['crp'])
                                  .filter(PsychologistHospitalModel.crp_psychologist_crp == PsychologistModel.crp)
                                  .filter(PsychologistHospitalModel.hospital_registry_number
                                          == HospitalModel.registry_number).all())

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

        new_pat_psycho_hosp = PatPsychoHospModel(psycho_hosp[0].id_psycho_hosp, new_patient.id_patient)
        new_pat_psycho_hosp.save_to_db()

        return {"message": "User created successfully."}, 201
