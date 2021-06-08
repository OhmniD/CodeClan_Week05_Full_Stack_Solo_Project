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
    driver_championship = driver_repository.driver_championship()
    team_championship = team_repository.team_championship_top_three()
    return render_template('index.html', driver_championship = driver_championship, team_championship=team_championship)

if __name__ == '__main__':
    app.run()