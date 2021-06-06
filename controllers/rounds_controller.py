from flask import Blueprint, Flask, redirect, render_template, request

from models.round import Round
import repositories.round_repository as round_repository

rounds_blueprint = Blueprint("rounds", __name__)

@rounds_blueprint.route("/rounds", methods=["GET"])
def all_rounds():
    rounds = round_repository.select_all()

    return render_template("/rounds/index.html", rounds=rounds)

@rounds_blueprint.route("/rounds/<id>", methods=["GET"])
def round_details(id):
    round = round_repository.select(id)
    return render_template("/rounds/show.html", round=round)