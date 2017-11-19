-- Teams
-- ~~~~~~~
--
-- Data on all teams currently participating in Vex Robotics Competition Events.

CREATE TABLE data_teams (
    id STRING PRIMARY KEY,              -- Team ID (i.e. 9181A)
    team_name STRING NOT NULL,          -- Team name
    robot_name STRING NOT NULL,         -- Robot name
    organization STRING,                -- Organization (typically school) team comes from
    city STRING NOT NULL,               -- City of origin
    region STRING NOT NULL,             -- Region of origin (province, state)
    country STRING NOT NULL,            -- Country
    grade STRING NOT NULL               -- Grade level (either middle or high school)
);
