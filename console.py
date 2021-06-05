import pdb

from models.driver import Driver
import repositories.driver_repository as driver_repository

from models.team import Team
import repositories.team_repository as team_repository

from models.driver_team import DriverTeam
import repositories.driver_team_repository as driver_team_repository

from models.round import Round
import repositories.round_repository as round_repository

## Driver repository tests and initial setup

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

team_repository.delete_all()

team1 = Team("McLaren", "Milton Keynes", 178, "Mercedes", "#ff9e1b", "static/images/teams/mclaren.jpg")
team_repository.save(team1)

all_teams = team_repository.select_all()

for team in all_teams:
    print(team.__dict__)

team1.championship_points = 203
team_repository.update(team1)

all_teams = team_repository.select_all()

for team in all_teams:
    print(team.__dict__)

## Testing drivers_teams join table works
driver_team_repository.delete_all()

driver1_team1 = DriverTeam(driver1, team1)
driver_team_repository.save(driver1_team1)

all_driver_team_relationships = driver_team_repository.select_all()

for team_driver in all_driver_team_relationships:
    print(team_driver.__dict__)

## Testing rounds methods

round_repository.delete_all()

round1 = Round("Interlagos", "Sao Paulo, Brazil", "2021-11-07", "static/images/tracks/interlagos.jpg")
round_repository.save(round1)

all_rounds = round_repository.select_all()

for round in all_rounds:
    print(round.__dict__)

round1.date = "2021-12-21"
round_repository.update(round1)

all_rounds = round_repository.select_all()

for round in all_rounds:
    print(round.__dict__)


pdb.set_trace()