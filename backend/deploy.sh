#!/bin/bash

docker build -t seminario-back:1.0 .
docker stack deploy -c docker-stack.yml seminario-back