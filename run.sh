#!/usr/bin/env bash


# source config.sh

# . .venv/bin/activate

# for var in "${VARS[@]}" ; do
#     KEY="${var%%:*}"
#     VALUE="${var##*:}"
#     export $KEY = $VALUE
#     echo $KEY = $VAUE
# done

flask run --host 0.0.0.0 --port 80