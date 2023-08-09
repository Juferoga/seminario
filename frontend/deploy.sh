#!/bin/bash

docker build -t seminario-front:1.0 .
docker stack deploy -c docker-stack.yml seminario-front