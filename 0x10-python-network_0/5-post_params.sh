#!/bin/bash
# Sends a `POST` request to the passed URL and display the body of response
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
