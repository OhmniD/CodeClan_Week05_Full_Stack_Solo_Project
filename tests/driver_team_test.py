import unittest
from models.driver_team import DriverTeam
from models.driver import Driver
from models.team import Team

class TestDriverTeam(unittest.TestCase):
    def setUp(self):
        self.driver = Driver("Lewis Hamilton", "British", 274, 44, "False", "static/images/drivers/lewis_hamilton.jpg")
        self.team = Team("Mercedes AMG Petronas", "Brackley, United Kingdom", 381, "Mercedes", "#00D2BE", "static/images/teams/mercedes.jpg")

        self.driver_team = DriverTeam(self.driver, self.team)

    def test_driver_team_has_a_driver(self):
        expected = "Lewis Hamilton"
        actual = self.driver_team.driver.name
        self.assertEqual(expected, actual)

    def test_driver_team_has_a_team(self):
        expected = "Mercedes AMG Petronas"
        actual = self.driver_team.team.name
        self.assertEqual(expected, actual)