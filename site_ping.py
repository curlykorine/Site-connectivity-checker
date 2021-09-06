import sys
import requests


def ping_site(url):
    r = requests.head(url)
    print(r.status_code)
    if r.status_code == 200:
        print("Site is available")
        return True
    else:
        print("Site is not available")
        return False

url = sys.argv[1]
ping_site(url)

#url = https://stackoverflow.com/ - status_code = 200, Site is available
#url = https://stackoverflow.com/asd - status_code = 404, Site is not available

#run this programm as 'python ./site_ping.py <url>'