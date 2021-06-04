DROP TABLE drivers_teams;
DROP TABLE entrants;
DROP TABLE race_results;
DROP TABLE rounds;
DROP TABLE drivers;
DROP TABLE teams;

CREATE TABLE drivers (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    nationality VARCHAR(255),
    championship_points VARCHAR(255),
    is_reserve BOOLEAN,
    picture_url VARCHAR(255)
);

CREATE TABLE teams (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    headquarters VARCHAR(255),
    championship_points VARCHAR(255),
    engine_supplier VARCHAR(255),
    team_colour VARCHAR(7),
    logo_url VARCHAR(255)
);

CREATE TABLE drivers_teams (
    id INT PRIMARY KEY,
    team_id INT REFERENCES teams(id) ON DELETE CASCADE,
    driver_id INT REFERENCES drivers(id) ON DELETE CASCADE
);

CREATE TABLE rounds (
    id INT PRIMARY KEY,
    track_name VARCHAR(255),
    track_location VARCHAR(255),
    date DATE,
    image_url VARCHAR(255)
);

CREATE TABLE entrants (
    id INT PRIMARY KEY,
    round_id INT REFERENCES rounds(id) ON DELETE CASCADE,
    team_id INT REFERENCES teams(id) ON DELETE CASCADE
);

CREATE TABLE race_results (
    id INT PRIMARY KEY,
    position INT,
    driver_id INT REFERENCES drivers(id) ON DELETE CASCADE,
    round_id INT REFERENCES rounds(id) ON DELETE CASCADE,
    fastest_lap BOOLEAN
);