__author__ = "Charlie Friend <charles.d.friend@gmail.com>"

import sys
import requests

API_BASE_URL = "https://api.vexdb.io/v1"


def get_num_teams(program):
    """ Get the number of teams on VexDB in a given program (VRC or VexU). """
    resp = requests.get(API_BASE_URL + "/get_teams", {"nodata": "true", "program": program})
    return int(resp.json()["size"])


def get_teams(program):
    """
    Gets data on a given number of teams from VexDB.

    :param program: VRC or VexU.
    :param start_ind: Starting index of teams to retrieve.
    :param num: Number of entries to retrive.
    :return: List of tuples containing team data.
    """
    ind = 0
    num_teams = get_num_teams(program)
    print "Found %d teams" % num_teams

    print "Getting team data from: " + API_BASE_URL + "/get_teams"

    team_data = []

    # get teams 1000 at a time (otherwise VexDB will truncate the list)
    while ind < num_teams:
        resp = requests.get(API_BASE_URL + "/get_teams",
                            {
                                "program": program,
                                "limit_start": ind,
                                "limit_number": 1000
                            })

        resp_data = resp.json()

        team_data.extend([
            (
                team["number"],
                team["team_name"],
                team["robot_name"],
                team["organisation"],
                team["city"],
                team["country"],
                team["region"],
                team["grade"]
            )
            for team in resp_data["result"]
        ])

        sys.stdout.write("\r%d%%" % (ind / float(num_teams) * 100))
        ind += 1000

    sys.stdout.write("\r100%\n")

    return team_data


def get_num_events(program, game):
    """ Get the number of events on VexDB for a given program (VRC or VexU) and game. """
    resp = requests.get(API_BASE_URL + "/get_events", {"nodata": "true", "program": program, "season": game})
    return int(resp.json()["size"])


def get_events(program, game):
    ind = 0
    num_events = get_num_events(program, game)
    print "Found %d events" % num_events

    print "Getting event data from: " + API_BASE_URL + "/get_events"

    event_data = []

    while ind < num_events:
        resp = requests.get(API_BASE_URL + "/get_events",
                            {
                                "program": program,
                                "limit_start": ind,
                                "limit_number": 1000
                            })

        resp_data = resp.json()

        event_data.extend([
            (
                team["sku"],
                team["name"],
                team["loc_venue"],
                team["loc_city"],
                team["loc_region"],
                team["loc_country"],
                team["start"],
                team["end"]
            )
            for team in resp_data["result"]
        ])

        sys.stdout.write("\r%d%%" % (ind / float(num_events) * 100))
        ind += 1000

    sys.stdout.write("\r100%\n")
    return event_data


def get_num_matches(program, game):
    """ Get the number of events on VexDB for a given program (VRC or VexU) and game. """
    resp = requests.get(API_BASE_URL + "/get_matches", {"nodata": "true", "program": program, "season": game})
    return int(resp.json()["size"])

def get_matches(program, game):
    ind = 0
    num_matches = get_num_matches(program, game)
    print "Found %d matches" % num_matches

    print "Getting match data from: " + API_BASE_URL + "/get_matches"

    match_data = []

    while ind < num_matches:
        resp = requests.get(API_BASE_URL + "/get_matches",
                            {
                                "program": program,
                                "limit_start": ind,
                                "limit_number": 1000
                            })

        resp_data = resp.json()

        match_data.extend([
            (
                match["sku"],
                match["red1"],
                match["red2"],
                match["red3"],
                match["redsit"],
                match["blue1"],
                match["blue2"],
                match["blue3"],
                match["bluesit"],
                match["redscore"],
                match["bluescore"],
                match["scheduled"]
            )
            for match in resp_data["result"]
        ])

        sys.stdout.write("\r%d%%" % (ind / float(num_matches) * 100))
        ind += 1000

    sys.stdout.write("\r100%\n")
    return match_data
