import unittest
from datetime import date

from fake_data.store import store_sensor

class TestStore(unittest.TestCase):

    def test_get_all_traffic(self):
        toulon_store = store_sensor('toulon', 1200, 300)
        visits = toulon_store.get_all_traffic(date(2025,8,12))

        self.assertEqual(visits, 1151)

    def test_get_sensor_traffic(self):
        toulon_store = store_sensor('toulon', 1200, 300)
        visits = toulon_store.get_sensor_traffic(2, date(2025,8,19))

        self.assertEqual(visits, 92)

    def test_sunday_close(self):
        toulon_store = store_sensor('toulon', 1200, 300)
        visits = toulon_store.get_all_traffic(date(2025,8,17))

        # Ici ce doit être à moins -8 car chaque magasin possède 8 capteurs
        self.assertEqual(visits, -8)

if __name__ == '__main__':
    unittest.main()