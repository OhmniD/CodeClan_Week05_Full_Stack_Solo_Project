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

@teams_blueprint.route("/teams", methods=["POST"])
def create_team():
    name = request.form['name']
    headquarters = request.form['headquarters']
    engine_supplier = request.form['engine_supplier']
    team_colour = request.form['team_colour']
    logo_url = request.form['logo_url']
    championship_points = 0
    team = Team(name, headquarters, championship_points, engine_supplier, team_colour, logo_url)
    team_repository.save(team)

    return redirect('/teams')

@teams_blueprint.route("/teams/<id>/delete", methods=["GET"])
def delete_team(id):
    team_repository.delete(id)
    return redirect('/teams')

@teams_blueprint.route("/teams/<id>/edit", methods=["GET"])
def edit_team(id):
    team = team_repository.select(id)
    return render_template("teams/edit.html", team=team)

@teams_blueprint.route("/teams/<id>", methods=["POST"])
def update_team(id):
    team = team_repository.select(id)
    name = request.form['name']
    headquarters = request.form['headquarters']
    championship_points = team.championship_points
    engine_supplier = request.form['engine_supplier']
    team_colour = request.form['team_colour']
    logo_url = request.form['logo_url']
    team = Team(name, headquarters, championship_points, engine_supplier, team_colour, logo_url, id)
    team_repository.update(team)
    return redirect('/teams')