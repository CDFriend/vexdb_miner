__author__ = "Charlie Friend <charles.d.friend@gmail.com>"

import os
import sqlite3
import sys
import requests
import vexdb_api


def main():
    # create new database (if one doesn't already exist)
    if not os.path.isfile("vexdb_data.sqlite"):
        conn = create_new_db()
    else:
        conn = sqlite3.connect("vexdb_data.sqlite")

    # get number of available teams
    num_teams = vexdb_api.get_num_teams("VRC")
    print "Found %d teams." % num_teams

    # get teams 1,000 entries at a time (VexDB tends to limit at around 5,000)
    teamnum = 0
    print "Getting VRC teams data from: " + vexdb_api.API_BASE_URL
    while teamnum < num_teams:
        # get team data (VEX Robotics Competition only) from vexdb.io
        team_data = vexdb_api.get_teams("VRC", teamnum, 1000)

        conn.executemany("INSERT OR REPLACE INTO data_teams VALUES (?, ?, ?, ?, ?, ?, ?, ?);", team_data)

        # update progress
        sys.stdout.write("\r %d%%" % int((float(teamnum) / num_teams) * 100))
        teamnum += 1000

    sys.stdout.write("\r100%\n")

    conn.commit()


def create_new_db():
    """
    Makes a new SQLite database and creates the appropriate tables from the schema/
    directory.

    Returns a connection to the new database.
    """
    conn = sqlite3.connect("vexdb_data.sqlite")

    _read_sql_file(conn, "schema/teams.sql")
    return conn


def _read_sql_file(conn, filename):
    """ Executes all statements in an SQL script. """
    with open(filename, 'rw') as file:
        for line in file.read().split(";"):
            conn.execute(line)

if __name__ == "__main__":
    main()
