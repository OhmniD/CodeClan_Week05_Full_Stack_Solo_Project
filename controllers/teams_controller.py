from flask import Blueprint, Flask, redirect, render_template, request

from models.team import Team
from models.driver_team import DriverTeam
import repositories.team_repository as team_repository
import repositories.driver_team_repository as driver_team_repository
import repositories.driver_repository as driver_repository

teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route("/teams", methods=["GET"])
def all_teams():
    teams = team_repository.select_all()

    return render_template("teams/index.html", teams=teams)

@teams_blueprint.route("/teams/<id>", methods=["GET"])
def team_details(id):
    team = team_repository.select(id)
    drivers = team_repository.drivers(team)

    return render_template("teams/show.html", team=team, drivers=drivers)

@teams_blueprint.route("/teams/new", methods=["GET"])
def new_team():
    return render_template("teams/new.html")
