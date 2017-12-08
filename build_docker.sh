#!/bin/bash
cp deploy-docker/Dockerfile ../
cp deploy-docker/docker-compose.yml ../
cd ../
docker-compose up -d --build
rm Dockerfile
