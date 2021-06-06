import pdb

from models.driver import Driver
import repositories.driver_repository as driver_repository

from models.team import Team
import repositories.team_repository as team_repository

from models.driver_team import DriverTeam
import repositories.driver_team_repository as driver_team_repository

from models.round import Round
import repositories.round_repository as round_repository

from models.entrant import Entrant
import repositories.entrant_repository as entrant_repository

from models.race_result import RaceResult
import repositories.race_result_repository as race_result_repository

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

## Testing entrants join table

entrant_repository.delete_all()

entrant1 = Entrant(round1, team1)
entrant_repository.save(entrant1)

all_entrants = entrant_repository.select_all()

for entrant in all_entrants:
    print(entrant.__dict__)

## Testing race_results table

race_result_repository.delete_all()

result1 = RaceResult(1, driver1, round1, "True")
race_result_repository.save(result1)

all_race_results = race_result_repository.select_all()

for race_result in all_race_results:
    print(race_result.__dict__)

## Testing retrieve team for driver functionality

driver1_team = driver_repository.team(driver1)

print(driver1_team)

## Adding some more data

driver2 = Driver("Lewis Hamilton", "British", 274, 44, "False", "static/images/drivers/lewis_hamilton.jpg")
driver_repository.save(driver2)
driver3 = Driver("Alex Albon", "Thai", 0, 23, "True", "static/images/drivers/alex_albon.jpg")
driver_repository.save(driver3)

team2 = Team("Mercedes AMG Petronas", "Brackley, United Kingdom", 381, "Mercedes", "#00D2BE", "static/images/teams/mercedes.jpg")
team_repository.save(team2)
team3 = Team("Red Bull Racing", "Milton Keynes, United Kingdom", 209, "Honda", "#0600EF", "static/images/teams/red_bull.jpg")
team_repository.save(team3)
team4 = Team("Alpha Tauri", "Faenza, Italy", 143, "Honda", "#2B4562", "static/images/teams/alpha_tauri.jpg")
team_repository.save(team4)

driver2_team2 = DriverTeam(driver2, team2)
driver3_team3 = DriverTeam(driver3, team3)
driver3_team4 = DriverTeam(driver3, team4)


driver_team_repository.save(driver2_team2)
driver_team_repository.save(driver3_team3)
driver_team_repository.save(driver3_team4)

championship = driver_repository.driver_championship()

for driver in championship:
    print(driver.__dict__)

pdb.set_trace()