import unittest

from models.race_result import RaceResult
from models.driver import Driver
from models.team import Team
from models.round import Round

class TestRaceResult(unittest.TestCase):
    def setUp(self):

        self.driver = driver1 = Driver("Lando Norris", "British", 78, 4, "False", "static/images/drivers/lando_norris.jpg")
        self.team = Team("Red Bull Racing", "Milton Keynes, United Kingdom", 209, "Honda", "#0600EF", "static/images/teams/red_bull.jpg")
        self.round = Round("Interlagos", "Sao Paulo, Brazil", "2021-11-07", "static/images/tracks/interlagos.jpg")

        self.race_result = RaceResult(3, self.driver, self.team, self.round, "True")

    def test_race_result_has_a_position(self):
        expected = 3
        actual = self.race_result.position
        self.assertEqual(expected, actual)
    
    def test_race_result_has_a_driver(self):
        expected = "British"
        actual = self.race_result.driver.nationality
        self.assertEqual(expected, actual)

    def test_race_result_has_a_team(self):
        expected = "Honda"
        actual = self.race_result.team.engine_supplier
        self.assertEqual(expected, actual)

    def test_race_result_has_a_round(self):
        expected = "Sao Paulo, Brazil"
        actual = self.race_result.round.track_location
        self.assertEqual(expected, actual)
        
    def test_race_result_has_a_fastest_lap_boolean(self):
        expected = "True"
        actual = self.race_result.fastest_lap
        self.assertEqual(expected, actual)

