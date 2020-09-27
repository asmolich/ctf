#!/usr/bin/env python

import requests
import re

url = "http://challenge.ctf.games:30095"

robots = "/robots.txt"

flag = {}
mini = 100000
maxi = -100000

def print_flag():
    res = []
    for i in range(max(mini, 0), min(maxi, 50) + 1):
        res.append(flag[i] if i in flag else "?")
    return "".join(res)

run = 0
while len(flag) < 35:
    run += 1
    if run % 10 == 0:
        print(f"flag so far: {print_flag()}")
    r = requests.get(url + robots)
    sections = r.text.split("\n\n")
    for section in sections:
        ua = None
        for line in section.split("\n"):
            #print(line)
            path = None
            if line.startswith("User"):
                ua = line[12:] # len("User-agent: ")
            else:
                path = line[10:] # len("Disallow: ")

            if ua and path:
                headers = {"User-Agent": ua}
                r = requests.get(url + path, headers=headers)
                #print(r.text)
                if r.text.startswith("REJOICE, ROBOT."):
                    m = re.finditer("INDEX (\d+)", r.text)
                    if m:
                        fidx, pidx = [match.group(1) for match in m]
                        ch = path[int(pidx) + 1]
                        fidx = int(fidx)
                        flag[fidx] = ch
                        print(f"flag[{fidx}] = {ch}")
                        mini = min(mini, fidx)
                        maxi = max(maxi, fidx)

print(f"Flag = {print_flag()}")

# flag{beep_boop_are_you_a_robot_too}

