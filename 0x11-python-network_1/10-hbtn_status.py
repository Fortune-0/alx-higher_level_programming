#!/usr/bin/python3
import urllib.request
"""Fetches https://alx-intranet.hbtn.io/status."""

# if __name__ == "__main__":
#    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
#        body = response.read()
#        print("Body response:")
#        print("\t- type: {}".format(type(body)))
#        print("\t- content: {}".format(body))
#        print("\t- utf8 content: {}".format(body.decode("utf-8")))


if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
