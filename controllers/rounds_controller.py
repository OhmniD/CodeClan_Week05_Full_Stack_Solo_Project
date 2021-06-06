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

@rounds_blueprint.route("/rounds/new", methods=["GET"])
def new_round():
    return render_template("/rounds/new.html")

@rounds_blueprint.route("/rounds", methods=["POST"])
def create_rounds():
    track_name = request.form['track_name']
    track_location = request.form['track_location']
    date = request.form['date']
    image_url = request.form['image_url']

    round = Round(track_name, track_location, date, image_url)
    round_repository.save(round)
    return redirect('/rounds')

@rounds_blueprint.route("/rounds/<id>/delete", methods=["GET"])
def delete_round(id):
    round_repository.delete(id)
    return redirect('/rounds')

@rounds_blueprint.route("/rounds/<id>/edit", methods=["GET"])
def edit_round(id):
    round = round_repository.select(id)
    return render_template("/rounds/edit.html", round=round)

@rounds_blueprint.route("/rounds/<id>", methods=["POST"])
def update_round(id):
    track_name = request.form['track_name']
    track_location = request.form['track_location']
    date = request.form['date']
    image_url = request.form['image_url']

    round = Round(track_name, track_location, date, image_url, id)
    round_repository.update(round)
    return redirect('/rounds')
