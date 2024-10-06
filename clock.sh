#!/usr/bin/env sh

# > Author:     Pablo Andrade
# > Created:    06/10/2024
# > Version:    0.1

case "$1" in
    "now") python3 /home/pablodeas/Projects/pessoal/Python/clock/main.py "$1"
    ;;
    "timer") python3 /home/pablodeas/Projects/pessoal/Python/clock/main.py "$1" "$2"
    ;;
esac
