DROP TABLE drivers_teams;
DROP TABLE entrants;
DROP TABLE race_results;
DROP TABLE rounds;
DROP TABLE drivers;
DROP TABLE teams;

CREATE TABLE drivers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    nationality VARCHAR(255),
    championship_points INT,
    car_number INT,
    is_reserve BOOLEAN,
    picture_url VARCHAR(255)
);

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    headquarters VARCHAR(255),
    championship_points INT,
    engine_supplier VARCHAR(255),
    team_colour VARCHAR(7),
    logo_url VARCHAR(255)
);

CREATE TABLE drivers_teams (
    id SERIAL PRIMARY KEY,
    team_id INT REFERENCES teams(id) ON DELETE CASCADE,
    driver_id INT REFERENCES drivers(id) ON DELETE CASCADE
);

CREATE TABLE rounds (
    id SERIAL PRIMARY KEY,
    track_name VARCHAR(255),
    track_location VARCHAR(255),
    date DATE,
    image_url VARCHAR(255)
);

CREATE TABLE entrants (
    id SERIAL PRIMARY KEY,
    round_id INT REFERENCES rounds(id) ON DELETE CASCADE,
    team_id INT REFERENCES teams(id) ON DELETE CASCADE
);

CREATE TABLE race_results (
    id SERIAL PRIMARY KEY,
    position INT,
    driver_id INT REFERENCES drivers(id) ON DELETE CASCADE,
    team_id INT REFERENCES teams(id) ON DELETE CASCADE,
    round_id INT REFERENCES rounds(id) ON DELETE CASCADE,
    fastest_lap BOOLEAN
);