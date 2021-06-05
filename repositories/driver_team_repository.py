from db.run_sql import run_sql

from models.driver_team import DriverTeam

from models.driver import Driver
import repositories.driver_repository as driver_repository

from models.team import Team
import repositories.team_repository as team_repository

def save(driver_team):
    sql = "INSERT INTO driver_team (driver_id, team_id) VALUES (%s, %s) returning id"
    values = [driver_team.driver.id, driver_team.team.id]
    result = run_sql(sql, values)
    id = result[0]['id']
    driver_team.id = id