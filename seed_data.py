import pdb

from models.driver import Driver
import repositories.driver_repository as driver_repository

from models.team import Team
import repositories.team_repository as team_repository

from models.driver_team import DriverTeam
import repositories.driver_team_repository as driver_team_repository

from models.round import Round
import repositories.round_repository as round_repository

driver_repository.delete_all()
team_repository.delete_all()
driver_team_repository.delete_all()
round_repository.delete_all()

driver1 = Driver("Lando Norris", "British", 0, 4, "False", "static/images/drivers/lando_norris.jpg")
driver2 = Driver("Daniel Ricciardo", "Australian", 0, 3, "False", "static/images/drivers/daniel_ricciardo.jpg")
driver3 = Driver("Sebastian Vettel", "German", 0, 5, "False", "static/images/drivers/sebastian_vettel.jpg")
driver4 = Driver("Lance Stroll", "Canadian", 0, 18, "False", "static/images/drivers/lance_stroll.jpg")
driver5 = Driver("Kimi Raikkonen", "Finnish", 0, 7, "False", "static/images/drivers/kimi_raikkonen.jpg")
driver6 = Driver("Antonio Giovinazzi", "Italian", 0, 99, "False", "static/images/drivers/antonio_giovinazzi.jpg")
driver7 = Driver("George Russell", "Britsh", 0, 63, "False", "static/images/drivers/george_russell.jpg")
driver8 = Driver("Nicholas Latifi", "Canadian", 0, 6, "False", "static/images/drivers/nicholas_latifi.jpg")
driver9 = Driver("Pierre Gasly", "French", 0, 10, "False", "static/images/drivers/pierre_gasly.jpg")
driver10 = Driver("Yuki Tsunoda", "Japanese", 0, 22, "False", "static/images/drivers/yuki_tsunoda.jpg")
driver11 = Driver("Charles Leclerc", "Monagasque", 0, 16, "False", "static/images/drivers/charles_leclerc.jpg")
driver12 = Driver("Carlos Sainz", "Spanish", 0, 55, "False", "static/images/drivers/carlos_sainz.jpg")
driver13 = Driver("Lewis Hamilton", "British", 0, 44, "False", "static/images/drivers/lewis_hamilton.jpg")
driver14 = Driver("Valterri Bottas", "Finnish", 0, 77, "False", "static/images/drivers/valterri_bottas.jpg")
driver15 = Driver("Esteban Ocon", "French", 0, 31, "False", "static/images/drivers/esteban_ocon.jpg")
driver16 = Driver("Fernando Alonso", "Spanish", 0, 14, "False", "static/images/drivers/fernando_alonso.jpg")
driver17 = Driver("Max Verstappen", "Dutch", 0, 33, "False", "static/images/drivers/max_verstappen.jpg")
driver18 = Driver("Sergio Perez", "Mexican", 0, 11, "False", "static/images/drivers/sergio_perez.jpg")
driver19 = Driver("Mick Schumacher", "German", 0, 47, "False", "static/images/drivers/mick_schumacher.jpg")
driver20 = Driver("Nikita Mazepin", "Russian", 0, 9, "False", "static/images/drivers/nikita_mazepin.jpg")

for x in range(1, 21, 1):
    driver_repository.save(eval('driver' + str(x)))

team1 = Team("McLaren", "Woking, United Kingdom", 0, "Mercedes", "#ff9e1b", "static/images/teams/mclaren.jpg")
team2 = Team("Alfa Romeo Racing", "Hinwil, Switzerland", 0, "Ferrari", "#900000", "static/images/teams/alfa_romeo.jpg")
team3 = Team("Aston Martin Cognizant", "Silverstone, United Kingdom", 0, "Mercedes", "#006F62", "static/images/teams/aston_martin.png")
team4 = Team("Williams Racing", "Grove, United Kingdom", 0, "Mercedes", "#005AFF", "static/images/teams/williams.jpg")
team5 = Team("AlphaTauri", "Faenza, Italy", 0, "Honda", "#2B4562", "static/images/teams/alphatauri.jpg")
team6 = Team("Red Bull Racing", "Milton Keynes, United Kingdom", 0, "Honda", "#0600EF", "static/images/teams/red_bull_racing.jpeg")
team7 = Team("Scuderia Ferrari", "Maranello, Italy", 0, "Ferrari", "#DC0000", "static/images/teams/ferrari.jpg")
team8 = Team("Alpine", "Enstone, United Kingdom", 0, "Renault", "#0090FF", "static/images/teams/alpine.jpg")
team9 = Team("Haas F1", "Kannapolis, United States", 0, "Ferrari", "#FFFFFF", "static/images/teams/haas.jpg")
team10 = Team("Mercedes-AMG Petronas", "Brackley, United Kingdom", 0, "Mercedes", "#00D2BE", "static/images/teams/mercedes.jpg")

for x in range(1, 11, 1):
    team_repository.save(eval('team' + str(x)))

driver_team1 = DriverTeam(driver1, team1)
driver_team2 = DriverTeam(driver2, team1)
driver_team3 = DriverTeam(driver3, team3)
driver_team4 = DriverTeam(driver4, team4)
driver_team5 = DriverTeam(driver5, team2)
driver_team6 = DriverTeam(driver6, team2)
driver_team7 = DriverTeam(driver7, team4)
driver_team8 = DriverTeam(driver8, team4)
driver_team9 = DriverTeam(driver9, team5)
driver_team10 = DriverTeam(driver10, team5)
driver_team11 = DriverTeam(driver11, team7)
driver_team12 = DriverTeam(driver12, team7)
driver_team13 = DriverTeam(driver13, team10)
driver_team14 = DriverTeam(driver14, team10)
driver_team15 = DriverTeam(driver15, team8)
driver_team16 = DriverTeam(driver16, team8)
driver_team17 = DriverTeam(driver17, team6)
driver_team18 = DriverTeam(driver18, team6)
driver_team19 = DriverTeam(driver19, team9)
driver_team20 = DriverTeam(driver20, team9)


for x in range(1, 21, 1):
    driver_team_repository.save(eval('driver_team' + str(x)))

round1 = Round("Interlagos", "Sao Paulo, Brazil", "2021-11-07", "static/images/tracks/interlagos.jpg")
round_repository.save(round1)