__author__ = "Charlie Friend <charles.d.friend@gmail.com>"

import os
import sqlite3
import sys
import vexdb_api


def main():
    # create new database (if one doesn't already exist)
    if not os.path.isfile("vexdb_data.sqlite"):
        conn = create_new_db()
    else:
        conn = sqlite3.connect("vexdb_data.sqlite")

    # get team data
    team_data = vexdb_api.get_teams("VRC")
    conn.executemany("INSERT OR REPLACE INTO data_teams VALUES (?, ?, ?, ?, ?, ?, ?, ?);", team_data)

    # get event data
    event_data = vexdb_api.get_events("VRC", "In The Zone")
    conn.executemany("INSERT OR REPLACE INTO data_events VALUES (?, ?, ?, ?, ?, ?, ?, ?);", event_data)

    # get match data
    match_data = vexdb_api.get_matches("VRC", "In The Zone")
    conn.executemany("INSERT OR REPLACE INTO data_matches VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", match_data)

    conn.commit()


def create_new_db():
    """
    Makes a new SQLite database and creates the appropriate tables from the schema/
    directory.

    Returns a connection to the new database.
    """
    conn = sqlite3.connect("vexdb_data.sqlite")

    _read_sql_file(conn, "schema/teams.sql")
    _read_sql_file(conn, "schema/events.sql")
    _read_sql_file(conn, "schema/matches.sql")

    return conn


def _read_sql_file(conn, filename):
    """ Executes all statements in an SQL script. """
    with open(filename, 'rb') as file:
        for line in file.read().split(";"):
            conn.execute(line)


if __name__ == "__main__":
    main()
