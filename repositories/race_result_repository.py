from db.run_sql import run_sql

from models.race_result import RaceResult

import repositories.driver_repository as driver_repository
import repositories.round_repository as round_repository

def save(race_result):
    sql = "INSERT INTO race_results (position, driver_id, round_id, fastest_lap) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [race_result.position, race_result.driver.id, race_result.round.id, race_result.fastest_lap]
    result = run_sql(sql, values)

    race_result.id = result[0]['id']

    return race_result

def select_all():
    race_results = []

    sql = "SELECT * FROM race_results"
    results = run_sql(sql)

    for row in results:
        driver = driver_repository.select(row['driver_id'])
        round = round_repository.select(row['round_id'])
        race_result = RaceResult(row['position'], driver, round, row['fastest_lap'], row['id'])
        race_results.append(race_result)
    
    return race_results

def select(id):
    race_result = NoneType

    sql = "SELECT * FROM race_results WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        driver = driver_repository.select(result['driver_id'])
        round = round_repository.select(result['round_id'])
        race_result = RaceResult(result['position'], driver, round, result['fastest_lap'], result['id'])
    
    return race_result

def update(race_result):
    sql = "UPDATE race_results SET (position, driver_id, round_id, fastest_lap) = (%s, %s, %s, %s) WHERE id = %s"
    values = [race_result.position, race_result.driver.id, race_result.round.id, race_result.fastest_lap, race_result.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM race_results"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM race_results WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def all_results_by_round(round_id):
    results_by_round = []

    sql = "SELECT * FROM race_results WHERE round_id = %s ORDER BY position ASC"
    values = [round_id]
    results = run_sql(sql, values)

    for row in results:
        id = row['id']
        position = row['position']
        fastest_lap = row['fastest_lap']
        driver = driver_repository.select(row['driver_id'])
        round = round_repository.select(row['round_id'])
        result = RaceResult(position, driver, round, fastest_lap, id)
        results_by_round.append(result)
    return results_by_round