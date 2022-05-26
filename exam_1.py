"""Exam 1."""
import requests


def check_server_status(ip):
    a = requests.get(ip)

    if a.status_code == 200:
        return True
    else:
        return False

assert check_server_status('https://github.com/') == True
print("skript is working")
