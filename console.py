import pdb

from models.driver import Driver
import repositories.driver_repository as driver_repository

from models.team import Team
import repositories.team_repository as team_repository

# Driver repository tests and initial setup

driver_repository.delete_all()

driver1 = Driver("Lando Norris", "British", 78, 4, "False", "static/images/drivers/lando_norris.jpg")

driver_repository.save(driver1)

all_drivers = driver_repository.select_all()

for driver in all_drivers:
    print(driver.__dict__)

driver1.championship_points = 103
driver_repository.update(driver1)

all_drivers = driver_repository.select_all()

for driver in all_drivers:
    print(driver.__dict__)

# Test that individual selection works - enter integer of valid row id to confirm
# print(driver_repository.select(1).__dict__)
## Team repository testing and initial setup
team1 = Team("McLaren", "Milton Keynes", 178, "Mercedes", "#ff9e1b", "static/images/teams/mclaren.jpg")
team_repository.save(team1)

all_teams = team_repository.select_all()

for team in all_teams:
    print(team.__dict__)


pdb.set_trace()