#!/bin/bash

URLS=(
"https://www.google.com"
"https://www.pinging.net"
)

# Pick a random url from the list
URL=${URLS[ $RANDOM % ${#URLS[@]} ]}

grep_response=$(grep zurg "/mnt/remote/realdebrid/version.txt")
external_status_code=$(curl --connect-timeout 10 -o /dev/null -s -w "%{http_code}" "$URL")

echo "External URL: $URL | external status code: $external_status_code | grep response: $grep_response"

if [ "$external_status_code" -eq 200 ] && [ "$grep_response" != "" ]; then
    exit 0
else
    exit 1
fi
