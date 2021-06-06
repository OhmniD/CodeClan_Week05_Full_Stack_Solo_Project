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