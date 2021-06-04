from db.run_sql import run_sql

from models.team import Team

def save(team):
    sql = "INSERT INTO teams(name, headquarters, championship_points, engine_supplier, team_colour, logo_url) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [team.name, team.headquarters, team.championship_points, team.engine_supplier, team.team_colour, team.logo_url]
    result = run_sql(sql, values)

    team.id = result[0]['id']

    return team