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
driver7 = Driver("George Russel", "Britsh", 0, 63, "False", "static/images/drivers/george_russell.jpg")
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