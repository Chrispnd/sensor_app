import unittest

from asttokens.util import visit_tree

from fake_data.sensor import capteur_visite
from datetime import date

class TestCapteurVisit(unittest.TestCase):

    def test_weekdays_open(self):
        for test_day in range(11, 17):
            with self.subTest(i = test_day):
                capteur = capteur_visite(1200, 300)
                visit_count = capteur.simulate_visit(date(2025, 8, test_day))

                self.assertFalse(visit_count == -1)

    def test_sunday_closed(self):
        capteur = capteur_visite(1200, 300)
        visit_count = capteur.simulate_visit(date(2025, 8, 17))

        self.assertEqual(visit_count, -1)

    def test_with_break(self):
        capteur = capteur_visite(1200, 300, perc_break = 1)
        visit_count = capteur.get_visit_count(date(2025, 8, 22))

        self.assertEqual(visit_count, 0)

    def test_with_malfunction(self):
        capteur = capteur_visite(1500, 150, perc_malfonction = 1)
        visit_count = capteur.get_visit_count(date(2025, 7, 26))

        self.assertEqual(visit_count, 391)

    def test_ferie_mai(self):
        capteur = capteur_visite(1200, 300)
        visit_count = capteur.get_visit_count(date(2025, 5, 1))

        self.assertEqual(visit_count, 0)

if __name__ == '__main__':
    unittest.main()