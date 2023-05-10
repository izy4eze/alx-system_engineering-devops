#!/usr/bin/python3
""" function to query a list of all hot posts on a given Reddit subreddit """
import requests from
after = None



def recurse(subreddit, hotlist=[]): 
    """returning top ten post tiltles recursively"""
    global after
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters {'after': after}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
