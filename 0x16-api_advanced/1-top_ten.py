#!/usr/bin/python3
"""
 Use Reddit API and prints the titles of
 the first 10 hot posts listed for a given subreddit
 example ./0-main.py apexlegends
"""
import requests


def top_ten(subreddit):
    """get top ten posts"""

    header = {"User-Agent": "kaelapp"}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        for post in r.json().get('data').get('children'):
            print(post.get('data').get('title'))
    else:
        return 0


if __name__ == "__main__":
    pass
