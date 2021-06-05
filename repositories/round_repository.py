from db.run_sql import run_sql

from models.round import Round

def save(round):
    sql = "INSERT INTO rounds (track_name, track_location, date, image_url) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [round.track_name, round.track_location, round.date, round.image_url]
    result = run_sql(sql, values)
    
    id = result[0]['id']
    round.id = id