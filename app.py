from flask import Flask, render_template

from controllers.drivers_controller import drivers_blueprint
from controllers.teams_controller import teams_blueprint

import repositories.driver_repository as driver_repository

app = Flask(__name__)

app.register_blueprint(drivers_blueprint)
app.register_blueprint(teams_blueprint)

@app.route('/')
def main():
    championship = driver_repository.championship_order()
    return render_template('index.html', championship = championship)

if __name__ == '__main__':
    app.run()