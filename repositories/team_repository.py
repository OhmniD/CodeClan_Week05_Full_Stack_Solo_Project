from db.run_sql import run_sql

from models.team import Team
from models.driver import Driver

def save(team):
    sql = "INSERT INTO teams(name, headquarters, championship_points, engine_supplier, team_colour, logo_url) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [team.name, team.headquarters, team.championship_points, team.engine_supplier, team.team_colour, team.logo_url]
    result = run_sql(sql, values)

    team.id = result[0]['id']

    return team

def select_all():
    teams = []

    sql = "SELECT * FROM teams ORDER BY name ASC"
    results = run_sql(sql)

    for row in results:
        team = Team(row['name'], row['headquarters'], row['championship_points'], row['engine_supplier'], row['team_colour'], row['logo_url'], row['id'])
        teams.append(team)

    return teams

def select(id):
    team = None

    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        team = Team(result['name'], result['headquarters'], result['championship_points'], result['engine_supplier'], result['team_colour'], result['logo_url'], result['id'])
    
    return team

def update(team):
    sql = "UPDATE teams SET (name, headquarters, championship_points, engine_supplier, team_colour, logo_url) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = values = [team.name, team.headquarters, team.championship_points, team.engine_supplier, team.team_colour, team.logo_url, team.id]
    result = run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def drivers(team):
    drivers = []

    sql = '''SELECT drivers.* FROM drivers
            INNER JOIN drivers_teams ON drivers_teams.driver_id = drivers.id 
            WHERE team_id = %s'''
    values = [team.id]
    results = run_sql(sql, values)

    for row in results:
        driver = Driver(row['name'], row['nationality'], row['championship_points'], row['car_number'], row['is_reserve'], row['picture_url'], row['id'])
        drivers.append(driver)

    return drivers