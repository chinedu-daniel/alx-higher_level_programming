#!/bin/bash
# Displays all HHTP methods
curl -sI "$1" | grep 'Allow:' | sed 's/^Allow: //'
