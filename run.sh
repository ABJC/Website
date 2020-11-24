#!/usr/bin/env bash


source config.sh

. .venv/bin/activate


for var in "${VARS[@]}" ; do
    KEY="${var%%:*}"
    VALUE="${var##*:}"
    echo "SETTING" $KEY
    export $KEY="$VALUE"
done

echo ""

flask run --host 0.0.0.0 --port 80