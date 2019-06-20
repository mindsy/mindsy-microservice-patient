from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from db import db
from resources.create_patient import RegisterPatient
from resources.edit_patient import EditPatient
from resources.pat_information import ShowAllInformationPatient, ShownPatientInformationID

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://mindsy:12345678@localhost:3306/MINDSY"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)
CORS(app)

api.add_resource(RegisterPatient, '/patient')
api.add_resource(ShowAllInformationPatient, '/patient/<string:crp>')
api.add_resource(ShownPatientInformationID, '/patient/<int:id>')
api.add_resource(EditPatient, '/patient/<int:id>')

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)

