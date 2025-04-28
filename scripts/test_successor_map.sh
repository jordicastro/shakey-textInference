#!/bin/bash

# TEST successor_map
# Usage: ./test_successor_map.sh

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

for N in {2..7}
do
  echo -e "Testing ${GREEN}$N${NC}-gram"
  python3 test_successor_map.py $N
done

echo "All n-grams tested successfully!"