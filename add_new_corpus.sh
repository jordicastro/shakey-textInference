#!/bin/bash

# ADD a new corpus to each ngram successor_map
# Usage: ./add_new_corpus.sh <filepath>
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <filepath>"
  exit 1
fi

FILEPATH=$1
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

if [ ! -f "$FILEPATH" ]; then
  echo "Error: File '$FILEPATH' not found."
  exit 1
fi

for N in {2..7}
do
  echo -e "Processing ${GREEN}$N${NC}-gram with file ${BLUE}$FILEPATH...${NC}"
  python3 ngrams.py $N "$FILEPATH"
done

echo "All n-grams processed successfully!"