#!/usr/bin/python3
"""Recursively collects the titles of all hot posts of a subreddit."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of all hot post titles, or None if subreddit is invalid.

    Calls itself once per page, passing the 'after' token to get the next one.
    """
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:alu.subs.checker:v1.0 (by /u/priscilla_alu)"
    }
    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)
    except requests.RequestException:
        return hot_list or None

    if response.status_code != 200:
        return hot_list or None

    try:
        data = response.json().get("data", {})
    except ValueError:
        return hot_list or None

    for child in data.get("children", []):
        hot_list.append(child.get("data", {}).get("title"))

    after = data.get("after")
    if after is None:
        return hot_list or None
    return recurse(subreddit, hot_list, after)
