import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.create_patient import RegisterPatient
from resources.pat_information import ShowAllInformationPatient, ShownPatientInformationID
from resources.edit_patient import EditPatient

app = Flask(__name__)
load_dotenv(".env")

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = os.environ.get("APP_SECRET_KEY")
app.config['JWT_SECRET_KEY'] = os.environ.get("APP_SECRET_KEY")

api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app)

api.add_resource(RegisterPatient, '/register-patient')
api.add_resource(ShowAllInformationPatient, '/list-patients/<string:crp>')
api.add_resource(ShownPatientInformationID, '/patient-information/<int:id>')
api.add_resource(EditPatient, '/edit-patient/<int:id>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True, host='0.0.0.0')
