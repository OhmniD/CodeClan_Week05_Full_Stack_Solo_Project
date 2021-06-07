import unittest
from models.driver import Driver


class TestDriver(unittest.TestCase):
    def setUp(self):

        self.driver = driver1 = Driver("Lando Norris", "British", 78, 4, "False", "static/images/drivers/lando_norris.jpg")

    def test_driver_has_a_name(self):
        expected = "Lando Norris"
        actual = self.driver.name
        self.assertEqual(expected, actual)

    def test_driver_has_a_nationality(self):
        expected = "British"
        actual = self.driver.nationality
        self.assertEqual(expected, actual)

    def test_driver_has_championship_points(self):
        expected = 78
        actual = self.driver.championship_points
        self.assertEqual(expected, actual)
    
    def test_driver_has_car_number(self):
        expected = 4
        actual = self.driver.car_number
        self.assertEqual(expected, actual)
    
    def test_if_driver_is_reserve(self):
        expected = "False"
        actual = self.driver.is_reserve
        self.assertEqual(expected, actual)

    def test_driver_has_picture_url(self):
        expected = "static/images/drivers/lando_norris.jpg"
        actual = self.driver.picture_url
        self.assertEqual(expected, actual)