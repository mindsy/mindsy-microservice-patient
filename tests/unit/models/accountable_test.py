from models.accountable import AccountableModel
from tests.base_test import BaseTest


class AccountableTest(BaseTest):
    def test_create_accountable(self):
        accountable = AccountableModel('11111111111', 'test', 1, 1)

        # registry_number_acc, kinship_degree, accountable_patient_id_patient, accountable_person_id

        self.assertEqual(accountable.registry_number_acc, '11111111111',
                         "The registry_number_acc of the accountable after creation "
                         "does not equal the constructor argument.")
        self.assertEqual(accountable.kinship_degree, 'test',
                         "The kinship_degree of the accountable_degree after creation "
                         "does not equal the constructor argument.")
        self.assertEqual(accountable.accountable_patient_id_patient, 1,
                         "The accountable_patient_id_patient of the accountable after creation "
                         "does not equal the constructor argument.")
        self.assertEqual(accountable.accountable_person_id, 1,
                         "The accountable_person_id of the accountable after creation does"
                         " not equal the constructor argument.")

        self.assertIsNone(accountable.accountable_person, "The 's accountable_person was not None even though "
                                                          "the store was not created.")
        self.assertIsNone(accountable.accountable_patient, "The accountable.accountable_patient "
                                                           "store was not None even though "
                                                           "the store was not created.")

    def test_accountable_json(self):
        accountable = AccountableModel('11111111111', 'test', 1, 1)
        expected = {
            'registry_number': accountable.registry_number_acc,
            'kinship_degree': accountable.kinship_degree
        }

        self.assertEqual(
            accountable.json(),
            expected,
            "The JSON export of the item is incorrect. Received {}, expected {}.".format(accountable.json(), expected))
