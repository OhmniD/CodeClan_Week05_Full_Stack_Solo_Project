import unittest

from models.round import Round

class TestRound(unittest.TestCase):
    def setUp(self):

        self.round = Round("Interlagos", "Sao Paulo, Brazil", "2021-11-07", "static/images/tracks/interlagos.jpg")


    def test_round_has_a_track_name(self):
        expected = "Interlagos"
        actual = self.round.track_name
        self.assertEqual(expected, actual)

    def test_round_has_a_track_location(self):
        expected = "Sao Paulo, Brazil"
        actual = self.round.track_location
        self.assertEqual(expected, actual)

    def test_round_has_a_date(self):
        expected = "2021-11-07"
        actual = self.round.date
        self.assertEqual(expected, actual)
    
    def test_round_has_an_image_url(self):
        expected = "static/images/tracks/interlagos.jpg"
        actual = self.round.image_url
        self.assertEqual(expected, actual)