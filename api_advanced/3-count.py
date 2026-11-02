#!/usr/bin/python3
"""Recursively counts keywords in the titles of a subreddit's hot posts."""
import requests


def print_counts(counts, word_list):
    """Print keyword totals, highest first, then A to Z, skipping zeros."""
    lowered = [word.lower() for word in word_list]
    totals = {}
    for word, count in counts.items():
        total = count * lowered.count(word)
        if total > 0:
            totals[word] = total
    for word in sorted(totals, key=lambda w: (-totals[w], w)):
        print("{}: {}".format(word, totals[word]))


def count_words(subreddit, word_list, after=None, counts=None):
    """Count keywords in all hot post titles of a subreddit and print them.

    Calls itself once per page, passing the 'after' token to get the next one.
    Prints nothing if the subreddit is invalid or no keyword matches.
    """
    if counts is None:
        counts = {word.lower(): 0 for word in word_list}

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
        if response.status_code != 200:
            print_counts(counts, word_list)
            return
        data = response.json().get("data", {})
    except (requests.RequestException, ValueError):
        print_counts(counts, word_list)
        return

    for child in data.get("children", []):
        title = child.get("data", {}).get("title") or ""
        for token in title.lower().split():
            if token in counts:
                counts[token] += 1

    after = data.get("after")
    if after is None:
        print_counts(counts, word_list)
        return
    count_words(subreddit, word_list, after, counts)
