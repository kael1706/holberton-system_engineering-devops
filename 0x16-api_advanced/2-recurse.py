#!/usr/bin/python3
"""
Use Reddit API and returns a list
containing the titles of all hot
articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], reddit_after=None):
    """all hot articles for a given subreddit"""

    header = {"User-Agent": "kaelapp"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if reddit_after:
        url += "?after={}".format(reddit_after)
    r = requests.get(url,
                     headers=header,
                     allow_redirects=False)

    if r.status_code != 200:
        return None

    reddit_after = r.json().get('data').get('after')

    for post in r.json().get('data').get('children'):
        hot_list.append(post.get('data').get('title'))

    if reddit_after:
        return recurse(subreddit, hot_list, reddit_after)

    return hot_list


if __name__ == "__main__":
    pass
