# Reddit API - Advanced

This project uses the Reddit API to query subreddit information with Python.

## Files

| File | Description |
|------|-------------|
| `0-subs.py` | Function that returns the total number of subscribers for a given subreddit, or 0 if the subreddit is invalid |
| `1-top_ten.py` | Function that prints the titles of the first 10 hot posts of a subreddit, or None if the subreddit is invalid |
| `2-recurse.py` | Recursive function that returns a list of the titles of all hot posts of a subreddit, or None if the subreddit is invalid |

## Requirements

- Python 3
- `requests` module (`pip3 install requests`)
- Code follows `pycodestyle` style

## Usage

```bash
python3 0-main.py programming
```
