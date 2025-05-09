#!/usr/bin/env bash

set -x

if [ "$BET_TYPE" = "e2e" ]; then
    pytest
elif [ "$BET_TYPE" = "perf" ]; then
    locust
else
    echo "Unknown BET_TYPE: $BET_TYPE"
    exit 1
fi

