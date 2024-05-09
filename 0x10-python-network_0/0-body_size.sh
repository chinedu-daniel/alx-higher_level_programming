#!/bin/bash
# creates a URL and sends the request so it can be displayed

curl -s I "$1" | grep  'Content-Length' | sed 's/^Content-Length: //'
