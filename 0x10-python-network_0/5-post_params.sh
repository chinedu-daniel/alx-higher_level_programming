#!/bin/bash
# sends POST request to the URL
curl -sd 'email=test@gmail.com&subject=I will always be here for PLD' "$1"
