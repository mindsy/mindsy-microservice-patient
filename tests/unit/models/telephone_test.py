from models.telephone import TelephoneModel
from tests.base_test import BaseTest


class TelephoneTest(BaseTest):
    def test_create_item(self):
        telephone = TelephoneModel(111111111, 'test', 1)

        self.assertEqual(telephone.number, 111111111,
                         "The number of the telephone after creation does not equal the constructor argument.")
        self.assertEqual(telephone.telephone_type, 'test',
                         "The telephone type of the telephone after creation does not equal the constructor argument.")
        self.assertEqual(telephone.tel_person_id, 1,
                         "The store_id of the item after creation does not equal the constructor argument.")
        self.assertIsNone(telephone.tel_person, "The item's store was not None even though the store was not created.")

    # def test_item_json(self):
    #     item = ItemModel('test', 19.99, 1)
    #     expected = {
    #         'name': 'test',
    #         'price': 19.99
    #     }
    #
    #     self.assertEqual(
    #         item.json(),
    #         expected,
    #         "The JSON export of the item is incorrect. Received {}, expected {}.".format(item.json(), expected))
