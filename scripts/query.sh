#!/bin/bash

# takes in ngram and num_prediction_words
# runs query.py script and returns string
# Usage: ./query.sh <ngram> <num_prediction_words> <context>
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <ngram> <num_prediction_words> <context>"
    exit 1
fi

NGRAM=$1
NUM_PREDICTION_WORDS=$2
CONTEXT=$3

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Pass the context as a single quoted string to Python
# cd into the directory of the script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"
# pwd
python3 query.py "$NGRAM" "$NUM_PREDICTION_WORDS" "$CONTEXT"