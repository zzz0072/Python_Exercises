#!/bin/sh

FILES=$(ls | grep -v "\\.py" | grep -v $(basename $0))
echo rm -i $FILES
rm -i $FILES
