from db.run_sql import run_sql

from models.driver_team import DriverTeam

from models.driver import Driver
import repositories.driver_repository as driver_repository

from models.team import Team
import repositories.team_repository as team_repository

def save(driver_team):
    sql = "INSERT INTO drivers_teams (driver_id, team_id) VALUES (%s, %s) returning id"
    values = [driver_team.driver.id, driver_team.team.id]
    result = run_sql(sql, values)
    id = result[0]['id']
    driver_team.id = id

def select_all():
    drivers_teams = []

    sql = "SELECT * FROM drivers_teams"
    results = run_sql(sql)

    for row in results:
        driver = driver_repository.select(row["driver_id"])
        team = team_repository.select(row["team_id"])
        driver_team = DriverTeam(driver, team, row["id"])
        drivers_teams.append(driver_team)
    
    return drivers_teams

def select(id):
    sql = "SELECT * FROM drivers_teams WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    driver = driver_repository.select(result["driver_id"])
    team = team_repository.select(result["team_id"])
    driver_team = DriverTeam(driver, team, result["id"])

    return driver_team

def update(driver_team):
    sql = "UPDATE drivers_teams SET (driver_id, team_id) = (%s, %s) WHERE id = %s"
    values = [driver_team.driver.id, driver_team.team.id, driver_team.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM drivers_teams"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM drivers_teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all_teams_for_driver(driver):
    sql = "DELETE FROM drivers_teams WHERE driver_id = %s"
    values = [driver.id]
    run_sql(sql, values)

# def delete_duplicate_relationships():
#     sql = "SELECT * FROM drivers_teams WHERE "
#     sql = '''DELETE FROM drivers_teams WHERE drivers_teams.id NOT IN 
#             (SELECT id FROM (SELECT DISTINCT ON (driver_id, team_id) * FROM drivers_teams) AS drivers_teams_duplicates)'''
#     run_sql(sql)

