from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.create_patient import RegisterPatient
from resources.pat_information import ShowInformationUserID

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'mindsy-cadastro-microservice'
app.config['JWT_SECRET_KEY'] = 'mindsy-microservice-register'

api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWTManager(app)

api.add_resource(RegisterPatient, '/register_patient')
api.add_resource(ShowInformationUserID, '/pat_information')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True, host='0.0.0.0')
