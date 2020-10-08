#!/bin/bash

#curl -v --insecure --http1.1 --raw https://localhost:8080/

curl -s --insecure --http1.1 --raw https://localhost:8080/ | tail -2 | head -1 | cut -c7-
