#!/bin/bash


# correct usage
if [ $# -ne 1 ]; then
    echo "Usage: $0 <k>"
    echo "k is the number of top n-grams to evaluate"
    exit 1
fi

# get the parameter k from the command line
k=$1
# if k is provided, pass it into evalMetrics.py, otherwise use the default value
if [ -z "$k" ]; then
    k=3
fi

echo "Evaluating models with top k = $k results"

# this script runs evalMetrics.py for each n-gram
for n in {2..7}; do
    python3 evalMetrics.py $n $k
done
