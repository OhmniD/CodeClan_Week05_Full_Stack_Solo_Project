from db.run_sql import run_sql

from models.round import Round

def save(round):
    sql = "INSERT INTO rounds (track_name, track_location, date, image_url) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [round.track_name, round.track_location, round.date, round.image_url]
    result = run_sql(sql, values)
    
    id = result[0]['id']
    round.id = id

def select_all():
    rounds = []

    sql = "SELECT * FROM rounds ORDER BY date ASC"
    results = run_sql(sql)

    for row in results:
        round = Round(row['track_name'], row['track_location'], row['date'], row['image_url'], row['id'])
        rounds.append(round)
    
    return rounds

def select(id):
    round = None

    sql = "SELECT * FROM rounds WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        round = Round(result['track_name'], result['track_location'], result['date'], result['image_url'], result['id'])
    
    return round

def update(round):
    sql = "UPDATE rounds SET (track_name, track_location, date, image_url) = (%s, %s, %s, %s) WHERE id = %s"
    values = [round.track_name, round.track_location, round.date, round.image_url, round.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM rounds"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM rounds WHERE id = %s"
    values = [id]
    run_sql(sql, values)






