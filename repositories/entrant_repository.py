from db.run_sql import run_sql

from models.entrant import Entrant

from models.round import Round
import repositories.round_repository as round_repository

from models.team import Team
import repositories.team_repository as team_repository

def save(entrant):
    sql = "INSERT INTO entrants (round_id, team_id) VALUES (%s, %s) returning id"
    values = [entrant.round.id, entrant.team.id]
    result = run_sql(sql, values)
    id = result[0]['id']
    entrant.id = id

def select_all():
    entrants = []

    sql = "SELECT * FROM entrants"
    results = run_sql(sql)

    for row in results:
        round = round_repository.select(row["round_id"])
        team = team_repository.select(row["team_id"])
        entrant = Entrant(round, team, row["id"])
        entrants.append(entrant)
    
    return entrants

def select(id):
    sql = "SELECT * FROM entrants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    round = round_repository.select(result["round_id"])
    team = team_repository.select(result["team_id"])
    entrant = Round(round, team, result["id"])

    return entrant

def update(entrant):
    sql = "UPDATE entrants SET (round_id, team_id) = (%s, %s) WHERE id = %s"
    values = [entrant.round.id, entrant.team.id, entrant.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM entrants"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM entrants WHERE id = %s"
    values = [id]
    run_sql(sql, values)