from flask import Blueprint, Flask, redirect, render_template, request

import repositories.driver_repository as driver_repository

drivers_blueprint = Blueprint("drivers", __name__)

## Question to ask - possible to get team per driver to show on main overview page? Or will have to store teams as attribute in object?

@drivers_blueprint.route("/drivers", methods=["GET"])
def drivers():
    drivers = driver_repository.select_all()

    return render_template("drivers/index.html", drivers=drivers)

@drivers_blueprint.route("/drivers/<id>",  methods=["GET"])
def driver(id):
    driver = driver_repository.select(id)
    teams = driver_repository.team(driver)
    
    return render_template("drivers/show.html", driver=driver, teams=teams)