class RaceResult:
    def __init__(self, position, driver, round, fastest_lap, id = None):
        self.position = position
        self.driver = driver
        self.round = round
        self.fastest_lap = fastest_lap
        self.id = id