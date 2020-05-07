#!/usr/bin/python3
"""
Use Reddit API and returns the number of subscribers.
example: ./0-main.py apexlegends
"""
import requests


def number_of_subscribers(subreddit):
    """number of subscribers"""

    header = {"User-Agent": "kaelapp"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        return r.json().get('data').get('subscribers')
    else:
        return 0


if __name__ == "__main__":
    pass
