import unittest
from models.team import Team


class TestTeam(unittest.TestCase):
    def setUp(self):

        self.team = Team("Red Bull Racing", "Milton Keynes, United Kingdom", 209, "Honda", "#0600EF", "static/images/teams/red_bull.jpg")

    def test_driver_has_a_name(self):
        expected = "Red Bull Racing"
        actual = self.team.name
        self.assertEqual(expected, actual)

    def test_driver_has_headquarters(self):
        expected = "Milton Keynes, United Kingdom"
        actual = self.team.headquarters
        self.assertEqual(expected, actual)

    def test_team_has_championship_points(self):
        expected = 209
        actual = self.team.championship_points
        self.assertEqual(expected, actual)

    def test_team_has_engine_supplier(self):
        expected = "Honda"
        actual = self.team.engine_supplier
        self.assertEqual(expected, actual)

    def test_team_has_hex_colour(self):
        expected = "#0600EF"
        actual = self.team.team_colour
        self.assertEqual(expected, actual)

    def test_team_has_logo_url(self):
        expected = "static/images/teams/red_bull.jpg"
        actual = self.team.logo_url
        self.assertEqual(expected, actual)