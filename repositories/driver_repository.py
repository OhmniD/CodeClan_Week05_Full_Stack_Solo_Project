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

def select(id):
    driver = None
    sql = "SELECT * FROM drivers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        driver = Driver(result['name'], result['nationality'], result['championship_points'], result['car_number'], result['is_reserve'], result['picture_url'], result['id'])

    return driver

def update(driver):
    sql = "UPDATE drivers SET (name, nationality, championship_points, car_number, is_reserve, picture_url) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [driver.name, driver.nationality, driver.championship_points, driver.car_number, driver.is_reserve, driver.picture_url, driver.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM drivers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM drivers WHERE id = %s"
    values = [id]
    run_sql(sql, values)
