#!usr/bin/python3

import urllib.request
import sys
"""Python script that takes in a url
    """

if __name__=="__main__":
    url = sys.argv[1]  # first argument is the URL to be checked
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))