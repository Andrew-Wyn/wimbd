#!/bin/bash
set -Eeuo pipefail

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
PYTHON=$(which python | head -1)

# take the first three arguments
JOBS="$1"
LOAD="$2"
OUTPUT="$3"
DATASET="$4"

# skip the first three parameters
shift 4

parallel -j $JOBS "$PYTHON $SCRIPT_DIR/map.py --load $LOAD --dataset $DATASET --in_file {}" ::: "$@" | $PYTHON $SCRIPT_DIR/reduce.py --outputdir $OUTPUT