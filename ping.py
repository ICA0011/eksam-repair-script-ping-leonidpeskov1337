import requests

def check_server_status(url):
    a = requests.get(url)
    if a.status_code  == 200:
        return True
    else:
        return False
