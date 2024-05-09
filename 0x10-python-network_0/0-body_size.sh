#!/bin/bash
# creates a URL and sends the request so it can be displayed
curl -sI "$1" | grep  'Content-Length' | sed 's/^Content-Length: //'
