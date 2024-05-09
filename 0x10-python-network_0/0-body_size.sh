#!/bin/bash
# creates a URL and sends the request so it can be displayed

curl -s I "$1" | grep -i  "Content-Length" | awk '{print $2}'
