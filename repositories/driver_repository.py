from db.run_sql import run_sql

from models.driver import Driver

def save(driver):
    sql = "INSERT INTO drivers(name, nationality, championship_points, car_number, is_reserve, picture_url) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [driver.name, driver.nationality, driver.championship_points, driver.car_number, driver.is_reserve, driver.picture_url]
    
    result = run_sql(sql, values)
    
    driver.id = result[0]['id']
    
    return driver

def select_all():
    drivers = []

    sql = "SELECT * FROM drivers"
    results = run_sql(sql)

    for row in results:
        driver = Driver(row['name'], row['nationality'], row['championship_points'], row['car_number'], row['is_reserve'], row['picture_url'], row['id'])
        drivers.append(driver)

    return drivers