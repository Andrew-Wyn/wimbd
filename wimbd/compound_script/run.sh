#!/bin/bash
set -Eeuo pipefail

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
PYTHON=$(which python | head -1)

# take the first two arguments 
LOAD="$1"
OUTPUT="$2"
DATASET="$3"

# skip the first two parameters
shift 3

parallel "$PYTHON $SCRIPT_DIR/map.py --load $LOAD --dataset $DATASET --in_file {}" ::: "$@" | $PYTHON $SCRIPT_DIR/reduce.py --outputdir $OUTPUT