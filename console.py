import pdb

from models.driver import Driver
import repositories.driver_repository as driver_repository

driver1 = Driver("Lando Norris", "British", 78, 4, "False", "static/images/drivers/lando_norris.jpg")

driver_repository.save(driver1)

pdb.set_trace()