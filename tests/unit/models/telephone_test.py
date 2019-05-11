from models.telephone import TelephoneModel
from tests.base_test import BaseTest


class TelephoneTest(BaseTest):
    def test_create_telephone(self):
        telephone = TelephoneModel('111111111', 'test', 1)

        self.assertEqual(telephone.number, '111111111',
                         "The number of the telephone after creation does not equal the constructor argument.")
        self.assertEqual(telephone.telephone_type, 'test',
                         "The telephone type of the telephone after creation does not equal the constructor argument.")
        self.assertEqual(telephone.tel_person_id, 1,
                         "The store_id of the item after creation does not equal the constructor argument.")
        self.assertIsNone(telephone.tel_person, "The telephone was not None.")

    def test_telephone_json(self):
         telephone = TelephoneModel('111111111', 'test', 1)
         expected = {
             'number': '111111111',
             'telephone_type': 'test'
         }

         self.assertEqual(
             telephone.json(),
             expected,
             "The JSON export of the item is incorrect. Received {}, expected {}.".format(telephone.json(), expected))
