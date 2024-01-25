#!/bin/bash
# Sends a request to a given URL and display the content size of the response
curl -s "$1" | wc -c
