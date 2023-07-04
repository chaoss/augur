#!/bin/bash

echo background process stop &
cd /home/ubuntu/github/8knot 
sudo docker-compose down >> down.log 2>>down.err
echo $(date +%T)
echo waiting 
wait 
echo startup up &
echo $(date +%T)
cd /home/ubuntu/github/8knot 
sudo docker-compose up --build --scale query-worker=6 --scale callback-worker=6 >> dup.log 2>>dup.err  
echo $(date +%T)
