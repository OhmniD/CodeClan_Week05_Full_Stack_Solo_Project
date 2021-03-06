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
    '2': '18',
    '3': '15',
    '4': '12',
    '5': '10',
    '6': '8',
    '7': '6',
    '8': '4',
    '9': '2',
    '10': '1',
    '11': '0',
    '12': '0',
    '13': '0',
    '14': '0',
    '15': '0',
    '16': '0',
    '17': '0',
    '18': '0',
    '19': '0',
    '20': '0',
}

@race_results_blueprint.route("/race_results", methods=["GET"])
def new_race_result():
    rounds = round_repository.select_all()
    drivers = driver_repository.select_all_excluding_reserves()
    return render_template("/race_results/index.html", rounds=rounds, drivers=drivers)

@race_results_blueprint.route("/race_results", methods=["POST"])
def save_race_result():
    for x in range(20, 0, -1):
        position = x
        driver_id = request.form[str(x)]
        driver = driver_repository.select(driver_id)
        team = driver_repository.team(driver)[0]
        round = round_repository.select(request.form['round'])
        fastest_lap = False
        if request.form['fastest_lap'] == str(x) and position <= 10:
            fastest_lap = True
            driver.championship_points += 1
        race_result = RaceResult(position, driver, team, round, fastest_lap)
        race_result_repository.save(race_result)
        driver.championship_points += int(points_system[str(x)])
        
        driver_repository.update(driver)

        teams = driver_repository.team(driver)
        for team in teams:
            team_repository.team_points(team)

    return redirect('/race_results')

    