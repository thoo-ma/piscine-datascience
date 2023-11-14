#!/bin/bash

run() {
    script_name=$1
    mprof_file="${script_name%.*}.mprof"

    echo "Running $script_name..."
    mprof run $script_name
    echo "Generating mprof plot..."
    mprof plot -o ${mprof_file}.png
    echo "Done! Plot saved as ${mprof_file}.png"
}

run scripts/loop_inside_connection.py
run scripts/loop_outside_connection.py
