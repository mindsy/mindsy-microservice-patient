# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, request
from flask_jwt_extended import jwt_required

from models.patiente import PatientModel 
from models.person import PersonModel
from models.telephone import TelephoneModel
from models.accountable import AccountableModel

# from models.pat_psycho_hosp import Pat_Psycho_HospModel

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
                        required=False
                        )

    #  {
    #     "name": "Daniel",
    #     "email": "danieldesousa40@bol.com.br",
    #     "number": 12345,
    #     "telephone_type": "fixo",
    #     "date_of_birth": "05/09/1999",
    #     "scholarit": "Superior",
    #     "observation": "Este paciente não sabe comunicar microserviço, seu observador tbm não. Amandinha tá ocupada.",
    #     "manual_domain": "destro",
    #     "registry_number_patient": "40028922",
    #     "registry_number_hospital": "111111",
    #     "crp": "123456"
    # }

    def post(self):
        data = RegisterPatient.parser.parse_args()

        if PersonModel.find_by_email(data['email']):
            return {"message": "A user with that email already exists"}, 400
        
        if PatientModel.find_by_registry_number(data['registry_number_patient']):
            return {"message": "A user with that registry number already exists"}, 400

        if AccountableModel.find_by_registry_number(data['registry_number_accountable']):
            return {"message": "A user with that registry number already exists"}, 400
        
        new_person = PersonModel(data['name'], data['email'])
        new_person.save_to_db()

        new_telephone = TelephoneModel(data['number'], data['telephone_type'], new_person)
        new_telephone.save_to_db()

        new_patient = PatientModel(data['scholarit'], data['observation'], 
        data['manual_domain'], data['registry_number_patient'], data['date_of_birth'], new_person.id)
        new_patient.save_to_db()

        new_accountable = AccountableModel(data['registry_number_accountable'], data['kinship_degree'], new_patient.id_patient, new_person.id)
        new_accountable.save_to_db()

        # new_pat_psycho_hosp = Pat_Psycho_HospModel(new_patient, data['id'])
        # new_pat_psycho_hosp.save_to_db()

        return {"message": "User created successfully."}, 201
