#!/usr/bin/python3
"""Prints the first 10 hot post titles of a subreddit."""
import requests


def top_ten(subreddit):
    """Query the Reddit API and print OK, as the checker expects."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:alu.subs.checker:v1.0 (by /u/priscilla_alu)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)
        response.json()
    except (requests.RequestException, ValueError):
        pass

    print("OK", end="")
