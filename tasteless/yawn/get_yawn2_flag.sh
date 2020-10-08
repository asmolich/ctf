#!/bin/bash

nghttp -v --no-verify-peer https://localhost:8080/ | grep tstlss{.*?} | sed -e 's/.*flag: //'

