from models.patiente import PatientModel
from tests.base_test import BaseTest


class PatientTest(BaseTest):
    def test_create_patient(self):
        patient = PatientModel('superior', 'observation', 'destro', '12345', '09/04/1995', 1)

        self.assertEqual(patient.scholarit, 'superior',
                         "The scholarit of the patient after creation does not equal the constructor argument.")
        self.assertEqual(patient.observation, 'observation',
                         "The observation of the patient after creation does not equal the constructor argument.")
        self.assertEqual(patient.manual_domain, 'destro',
                         "The manual domain of the patient after creation does not equal the constructor argument.")
        self.assertEqual(patient.registry_number_pat, '12345',
                         "The registry number of the patient after creation does not equal the constructor argument.")
        self.assertEqual(patient.dt_birth, '09/04/1995',
                         "The date of birth of the patient after creation does not equal the constructor argument.")
        self.assertEqual(patient.person_pat_id, 1,
                         "The person_pat_id of the item after creation does not equal the constructor argument.")
        self.assertIsNone(patient.person_pat, "The person was not None.")
        self.assertListEqual(patient.accountables.all(), [],
                             "The patient's accountable length was not 0 even though no accountable were added.")

    def test_patient_json(self):
         patient = PatientModel('superior', 'observation', 'destro', '12345', '09/04/1995', 1)
         expected = {
          'id': None,
          'scholarit': 'superior',
          'observation': 'observation',
          'manual_domain': 'destro',
          'registry number': '12345',
          'date of birth': '09/04/1995',
          'accountables': []
         }

         self.assertEqual(
             patient.json(),
             expected,
             "The JSON export of the item is incorrect. Received {}, expected {}.".format(patient.json(), expected))