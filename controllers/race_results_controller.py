from flask import Blueprint, Flask, redirect, render_template, request

from models.driver import Driver
from models.driver_team import DriverTeam
from models.team import Team
from models.race_result import RaceResult

import repositories.driver_repository as driver_repository
import repositories.driver_team_repository as driver_team_repository
import repositories.team_repository as team_repository
import repositories.round_repository as round_repository
import repositories.race_result_repository as race_result_repository


race_results_blueprint = Blueprint("race_results", __name__)

points_system = {
    '1': '25',
    '2': '18'
}

@race_results_blueprint.route("/race_results", methods=["GET"])
def new_race_result():
    rounds = round_repository.select_all()
    drivers = driver_repository.select_all()
    return render_template("/race_results/index.html", rounds=rounds, drivers=drivers)

@race_results_blueprint.route("/race_results", methods=["POST"])
def save_race_result():
    for x in range(2, 0, -1):
        position = x
        driver_id = request.form[str(x)]
        driver = driver_repository.select(driver_id)
        round = round_repository.select(request.form['round'])
        fastest_lap = False
        race_result = RaceResult(position, driver, round, fastest_lap)
        race_result_repository.save(race_result)

        driver.championship_points += int(points_system[str(x)])
        if request.form['fastest_lap'] == 'on' and position <= 10:
            driver.championship_points += 1
        teams = driver_repository.team(driver)
        for team in teams:
            team_repository.team_points(team)
        driver_repository.update(driver)

        teams = driver_repository.team(driver)
        for team in teams:
            team_repository.team_points(team)

    return redirect('/race_results')

    