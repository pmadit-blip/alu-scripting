#!/usr/bin/python3
"""Queries the Reddit API for a subreddit's subscriber count."""
import requests


def number_of_subscribers(subreddit):
    """Return the total subscribers of a subreddit, or 0 if invalid."""
    if not isinstance(subreddit, str) or not subreddit:
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "python:alu.subs.checker:v1.0 (by /u/priscilla_alu)"
    }

    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False, timeout=10)
    except requests.RequestException:
        return 0

    if response.status_code != 200:
        return 0

    try:
        return response.json().get("data", {}).get("subscribers", 0)
    except ValueError:
        return 0
