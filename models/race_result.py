class RaceResult:
    def __init__(self, position, driver, team, round, fastest_lap, id = None):
        self.position = position
        self.driver = driver
        self.team = team
        self.round = round
        self.fastest_lap = fastest_lap
        self.id = id