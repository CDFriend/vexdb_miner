__author__ = "Charlie Friend <charles.d.friend@gmail.com>"

import requests

API_BASE_URL = "https://api.vexdb.io/v1"


def get_num_teams(program):
    """ Get the number of teams on VexDB in a given program (VRC or VexU). """
    resp = requests.get(API_BASE_URL + "/get_teams", {"nodata": "true", "program": program})
    return int(resp.json()["size"])


def get_teams(program, start_ind, num):
    """
    Gets data on a given number of teams from VexDB.

    :param program: VRC or VexU.
    :param start_ind: Starting index of teams to retrieve.
    :param num: Number of entries to retrive.
    :return: List of tuples containing team data.
    """
    resp = requests.get(API_BASE_URL + "/get_teams",
                        {
                            "program": program,
                            "limit_start": start_ind,
                            "limit_number": num
                        })

    resp_data = resp.json()

    # prepare data and add to database
    return [
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
    ]
