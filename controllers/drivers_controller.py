from flask import Blueprint, Flask, redirect, render_template, request
import sys

from models.driver import Driver
from models.driver_team import DriverTeam
import repositories.driver_repository as driver_repository
import repositories.driver_team_repository as driver_team_repository
import repositories.team_repository as team_repository
import repositories.race_result_repository as race_result_repository

drivers_blueprint = Blueprint("drivers", __name__)

## Question to ask - possible to get team per driver to show on main overview page? Or will have to store teams as attribute in object?

@drivers_blueprint.route("/drivers", methods=["GET"])
def all_drivers():
    drivers = driver_repository.select_all()

    return render_template("drivers/index.html", drivers=drivers)


@drivers_blueprint.route("/drivers/<id>",  methods=["GET"])
def driver_details(id):
    driver = driver_repository.select(id)
    teams = driver_repository.team(driver)
    
    return render_template("drivers/show.html", driver=driver, teams=teams)

@drivers_blueprint.route("/drivers/new", methods=["GET"])
def new_driver():
    teams = team_repository.select_all()
    return render_template("drivers/new.html", teams=teams)

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

    teams_list = request.form.getlist('team_id')
    print(teams_list, file=sys.stderr)
    for teams in teams_list:
        team_id = teams
        team = team_repository.select(team_id)
        driver_team = DriverTeam(driver, team)
        driver_team_repository.save(driver_team)

    return redirect('/drivers')

@drivers_blueprint.route("/drivers/<id>/delete", methods=["GET"])
def delete_driver(id):
    driver_repository.delete(id)
    return redirect('/drivers')

@drivers_blueprint.route("/drivers/<id>/edit", methods=["GET"])
def edit_driver(id):
    driver = driver_repository.select(id)
    teams = team_repository.select_all()
    driver_teams = driver_repository.team(driver)
    return render_template("drivers/edit.html", teams=teams, driver=driver, driver_teams=driver_teams)

@drivers_blueprint.route("/drivers/<id>", methods=["POST"])
def update_driver(id):
    name = request.form['name']
    nationality = request.form['nationality']
    championship_points = request.form['championship_points']
    car_number = request.form['car_number']
    is_reserve = True if 'is_reserve' in request.form else False
    picture_url = request.form['picture_url']
    driver = Driver(name, nationality, championship_points, car_number, is_reserve, picture_url, id)
    driver_repository.update(driver)

    driver_team_repository.delete_all_teams_for_driver(driver)

    teams_list = request.form.getlist('team_id')
    print(teams_list, file=sys.stderr)
    for teams in teams_list:
        team_id = teams
        team = team_repository.select(team_id)
        driver_team = DriverTeam(driver, team)
        driver_team_repository.save(driver_team)

    return redirect('/drivers')

@drivers_blueprint.route("/drivers/<id>/results", methods=["GET"])
def view_driver_results(id):
    results = race_result_repository.all_results_by_driver(id)
    return render_template("/rounds/results.html", results=results)
