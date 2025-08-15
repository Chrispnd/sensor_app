import unittest

from fake_data.sensor import sensor_visit
from datetime import date

class Testsensor_visitVisit(unittest.TestCase):

    def test_weekdays_open(self):
        for test_day in range(11, 17):
            with self.subTest(i = test_day):
                sensor = sensor_visit(1200, 300)
                visit_count = sensor.simulate_visit(date(2025, 8, test_day))

                self.assertFalse(visit_count == -1)

    def test_sunday_closed(self):
        sensor = sensor_visit(1200, 300)
        visit_count = sensor.simulate_visit(date(2025, 8, 17))

        self.assertEqual(visit_count, -1)

    def test_with_break(self):
        sensor = sensor_visit(1200, 300, perc_break = 1)
        visit_count = sensor.get_visit_count(date(2025, 8, 22))

        self.assertEqual(visit_count, 0)

    def test_with_malfunction(self):
        sensor = sensor_visit(1500, 150, perc_malfunction = 1)
        visit_count = sensor.get_visit_count(date(2025, 7, 26))

        self.assertEqual(visit_count, 391)

    def test_ferie_mai(self):
        sensor = sensor_visit(1200, 300)
        visit_count = sensor.get_visit_count(date(2025, 5, 1))

        self.assertEqual(visit_count, 0)

if __name__ == '__main__':
    unittest.main()