#!/bin/bash

echo "starting"

cd ..

rm -rf local_copy

scp -r /Users/$USER/Documents/projects/weather-lamp pi@weatherlight.local:/home/pi/weather-lamp

echo "finished"