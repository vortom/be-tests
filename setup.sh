#!/usr/bin/env bash
 
set -ex

if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

source .venv/bin/activate

pip install --upgrade pip
pip install --no-cache-dir --upgrade --force-reinstall -r ./requirements.txt
 
git submodule init
git submodule update
