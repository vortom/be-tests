#!/usr/bin/env bash

set -x

while IFS= read -r line; do
    # Skip empty lines and comments
    [[ -z "$line" || "$line" == \#* ]] && continue
    export "$line"
done < .env

if [ "$BET_TYPE" = "e2e" ]; then
    pytest
elif [ "$BET_TYPE" = "perf" ]; then
    locust
else
    echo "Unknown BET_TYPE: $BET_TYPE"
    exit 1
fi
