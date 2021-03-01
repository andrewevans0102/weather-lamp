#!/bin/bash

rm -rf local_copy

scp -r pi@weatherlight.local:/home/pi /Users/$USER/Documents/projects/weather-lamp/local_copy