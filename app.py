from flask import Flask, render_template

from controllers.drivers_controller import drivers_blueprint
from controllers.teams_controller import teams_blueprint
from controllers.rounds_controller import rounds_blueprint
from controllers.race_results_controller import race_results_blueprint

import repositories.driver_repository as driver_repository
import repositories.team_repository as team_repository

app = Flask(__name__)

app.register_blueprint(race_results_blueprint)
app.register_blueprint(drivers_blueprint)
app.register_blueprint(teams_blueprint)
app.register_blueprint(rounds_blueprint)


@app.route('/')
def main():
    driver_championship = driver_repository.driver_championship_top_three_inc_teams()
    team_championship = team_repository.team_championship_top_three()
    return render_template('index.html', driver_championship = driver_championship, team_championship=team_championship)

@app.route('/team_standings')
def team_standings():
    team_championship = team_repository.team_championship()
    return render_template('team_standings.html', team_championship=team_championship)

@app.route('/driver_standings')
def driver_standings():
    driver_championship = driver_repository.driver_championship_inc_teams()
    return render_template('driver_standings.html', driver_championship=driver_championship)

if __name__ == '__main__':
    app.run()