
class Driver:
    def __init__(self, name, nationality, championship_points, car_number, is_reserve, picture_url, id = None):
        self.name = name
        self.nationality = nationality
        self.championship_points = championship_points
        self.car_number = car_number
        self.is_reserve = is_reserve
        self.picture_url = picture_url
        self.id = id
        self.teams = []