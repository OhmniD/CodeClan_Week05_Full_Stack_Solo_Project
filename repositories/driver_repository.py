from db.run_sql import run_sql

from models.driver import Driver

def save(driver):
    sql = "INSERT INTO drivers(name, nationality, championship_points, car_number, is_reserve, picture_url) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [driver.name, driver.nationality, driver.championship_points, driver.car_number, driver.is_reserve, driver.picture_url]
    
    result = run_sql(sql, values)
    
    driver.id = result[0]['id']
    
    return driver