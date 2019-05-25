# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, request
from flask_jwt_extended import jwt_required
from models.patient import PatientModel
from datetime import datetime


class EditPatient(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('status',
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
                        type=str,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('telephone_type',
                        type=str,
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
    parser.add_argument('date_of_birth',
                        type=lambda d: datetime.strptime(d, '%d-%m-%Y')
                        )
    parser.add_argument('kinship_degree',
                        type=str,
                        required=False
                        )
    parser.add_argument('registry_number_acc',
                        type=str,
                        required=False
                        )

    def put(self, id):
        data = EditPatient.parser.parse_args()

        patient = PatientModel.find_by_id(id)

        if patient:
            if data['name']:
                if len(data['name']) <= 1:
                    return {"message": "Type a valid name"}
                patient.PERSON.name = data['name']

            if data['email']:
                patient.PERSON.email = data['email']

            if data['number']:
                if len(data['number']) > 15 or len(data['number']) < 8 or not data['number'].isdigit():
                    return {"message": "Type a valid telephone_number"}
                patient.PERSON.telephones[0].number = data['number']

            if data['telephone_type']:
                if str(data['telephone_type'].lower()) != str("residencial") and str(
                        data['telephone_type'].lower()) != str(
                        "pessoal") \
                        and str(data['telephone_type'].lower()) != str("comercial"):
                    return {"message": "Type a valid telephone_type"}
                patient.PERSON.telephones[0].telephone_type = data['telephone_type']

            if data['status']:
                if str(data['status'].lower()) != str("andamento") and str(data['status'].lower()) != str(
                        "aguardando") \
                        and str(data['status'].lower()) != str("finalizado"):
                    return {"message": "Type a valid status"}
                patient.status = data['status']

            if data['scholarity']:
                patient.scholarity = data['scholarity']

            if data['observation']:
                patient.observation = data['observation']

            if data['manual_domain']:
                if str(data['manual_domain'].lower()) != str("destro") and str(data['manual_domain'].lower()) != str(
                        "canhoto"):
                    return {"message": "Type a valid manual_domain"}
                patient.manual_domain = data['manual_domain']

            if data['registry_number_pat']:
                patient.registry_number_pat = data['registry_number_pat']

            if data['kinship_degree']:
                patient.ACCOUNTABLE.kinship_degree = data['kinship_degree']

            if data['registry_number_acc']:
                return {"message": "You cannot change this"}

            if data['date_of_birth']:
                patient.dt_birth = data['date_of_birth']
        else:
            return {'message': 'User not found.'}, 404

        patient.save_to_db()

        return {'message': 'User updated'}, 200
