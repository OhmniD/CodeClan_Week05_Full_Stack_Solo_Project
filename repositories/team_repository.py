from db.run_sql import run_sql

from models.team import Team

def save(team):
    sql = "INSERT INTO teams(name, headquarters, championship_points, engine_supplier, team_colour, logo_url) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [team.name, team.headquarters, team.championship_points, team.engine_supplier, team.team_colour, team.logo_url]
    result = run_sql(sql, values)

    team.id = result[0]['id']

    return team

def select_all():
    teams = []

    sql = "SELECT * FROM teams"
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
        team = Team(row['name'], row['headquarters'], row['championship_points'], row['engine_supplier'], row['team_colour'], row['logo_url'], row['id'])
    
    return team