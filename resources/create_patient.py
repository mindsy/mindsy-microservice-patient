# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, request
from flask_jwt_extended import jwt_required

from models.patiente import PatientModel 
from models.person import PersonModel
from models.telephone import TelephoneModel
from models.accountable import AccountableModel
from models.pat_psycho_hosp import Pat_Psycho_HospModel
from models.psychologist_hospital import PsychologistHospitalModel

class RegisterPatient(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name',
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
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('telephone_type',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('date_of_birth',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('kinship_degree',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('scholarit',
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
    parser.add_argument('registry_number_patient',
                        type=str,
                        required=False
                        )
    parser.add_argument('registry_number_accountable',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('id',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )

    # {
    #     "name": "Daniel",
    #     "email": "daniel@bol.com.br",
    #     "number": "666666",
    #     "telephone_type": "residencial",
    #     "date_of_birth": "05/09/1999",
    #     "scholarit": "Superior",
    #     "observation": "Isso é uma observação",
    #     "manual_domain": "mae",
    #     "kinship_degree": "destro",
    #     "registry_number_accountable": "999904",
    #     "id": 1
    # }

    def post(self):
        data = RegisterPatient.parser.parse_args()

        if PersonModel.find_by_email(data['email']):
            return {"message": "A user with that email already exists"}, 400
        
        # if PatientModel.find_by_registry_number_pat(data['registry_number_patient']) or data['registry_number_patient'] != None:
        #     return {"message": "A user with that registry number patient already exists"}, 400

        # if AccountableModel.find_by_registry_number_acc(data['registry_number_accountable']):
        #     return {"message": "A user with that registry number accountable already exists"}, 400
        
        new_person = PersonModel(data['name'], data['email'])
        new_person.save_to_db()

        new_telephone = TelephoneModel(data['number'], data['telephone_type'], new_person)
        new_telephone.save_to_db()

        new_patient = PatientModel(data['scholarit'], data['observation'], 
        data['manual_domain'], data['registry_number_patient'], data['date_of_birth'], new_person)
        new_patient.save_to_db()

        new_accountable = AccountableModel(data['registry_number_accountable'], data['kinship_degree'],new_patient, new_person)
        new_accountable.save_to_db()

        new_pat_psycho_hosp = Pat_Psycho_HospModel(data['id'], new_patient)
        new_pat_psycho_hosp.save_to_db()

        return {"message": "User created successfully."}, 201
