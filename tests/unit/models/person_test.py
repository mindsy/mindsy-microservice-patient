from models.person import PersonModel
from tests.base_test import BaseTest


class PersonTest(BaseTest):
    def test_create_item(self):
        person = PersonModel('test', 'testel@teste.com')

        self.assertEqual(person.name, 'test',
                         "The name of the person after creation does not equal the constructor argument.")
        self.assertEqual(person.email, 'testel@teste.com',
                         "The email of the person after creation does not equal the constructor argument.")

        self.assertListEqual(person.telephones.all(), [],
                             "The person's telephone length was not 0 even though no telephones were added.")

    #    self.assertListEqual(person.patients.all(), [],
    #                          "The person's patients length was not 0 even though no patients were added.")
    #    self.assertListEqual(person.accountables.all(), [],
    #                          "The person's accountable length was not 0 even though no accountable were added.")

    def test_item_json(self):
        person = PersonModel('test', 'testel@teste.com')
        expected = {
            'name': 'test',
            'id': None,
            'email': 'testel@teste.com',
            'telephone': []
        }

        self.assertEqual(
             person.json(),
             expected,
             "The JSON export of the item is incorrect. Received {}, expected {}.".format(person.json(), expected))
