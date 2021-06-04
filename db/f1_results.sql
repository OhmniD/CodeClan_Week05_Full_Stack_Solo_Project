DROP TABLE driver_team;
DROP TABLE drivers;
DROP TABLE teams;
-- DROP TABLE
-- DROP TABLE
-- DROP TABLE

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

CREATE TABLE driver_team (
    id INT PRIMARY KEY,
    team_id INT REFERENCES teams(id) ON DELETE CASCADE,
    driver_id INT REFERENCES drivers(id) ON DELETE CASCADE
);