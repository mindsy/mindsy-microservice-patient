# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, request
from flask_jwt_extended import jwt_required

from models.patient import PatientModel


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
                patient.person_pat.name = data['name']
            if data['email']:
                patient.person_pat.email = data['email']
            if data['number']:
                patient.person_pat.telephones[0].number = data['number']
            if data['scholarity']:
                patient.scholarity = data['scholarity']
            if data['observation']:
                patient.observation = data['observation']
            if data['manual_domain']:
                patient.manual_domain = data['manual_domain']
            if data['registry_number_pat']:
                patient.registry_number_pat = data['registry_number_pat']
            if data['kinship_degree']:
                patient.accountables.kinship_degree = data['kinship_degree']
            if data['registry_number_acc']:
                patient.accountables.registry_number_acc = data['registry_number_acc']
        else:
            return {'message': 'User not found.'}, 404

        patient.save_to_db()

        return {'message': 'User updated'}, 200
