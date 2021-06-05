from flask import Blueprint, Flask, redirect, render_template, request

from models.driver import Driver
import repositories.driver_repository as driver_repository

drivers_blueprint = Blueprint("drivers", __name__)

## Question to ask - possible to get team per driver to show on main overview page? Or will have to store teams as attribute in object?

@drivers_blueprint.route("/drivers", methods=["GET"])
def all_drivers():
    drivers = driver_repository.select_all()

    return render_template("drivers/index.html", drivers=drivers)

@drivers_blueprint.route("/drivers/new", methods=["GET"])
def new_driver():
    return render_template("drivers/new.html")

@drivers_blueprint.route("/drivers/<id>",  methods=["GET"])
def driver_details(id):
    driver = driver_repository.select(id)
    teams = driver_repository.team(driver)
    
    return render_template("drivers/show.html", driver=driver, teams=teams)

@drivers_blueprint.route("/drivers", methods=["POST"])
def create_driver():
    name = request.form['name']
    nationality = request.form['nationality']
    car_number = request.form['car_number']
    is_reserve = True if 'is_reserve' in request.form else False
    picture_url = request.form['picture_url']
    championship_points = 0
    driver = Driver(name, nationality, championship_points, car_number, is_reserve, picture_url)
    driver_repository.save(driver)
    return redirect('/drivers')