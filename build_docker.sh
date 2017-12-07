#!/bin/bash
if [ $# != 1 ] ; then
  echo "USAGE: ./build_docker.sh v1.0.0"
  exit 1;
fi
cp deploy-docker/Dockerfile ../
cd ../
docker build -t syl/jobplus:$1 .
rm Dockerfile
docker run -d -p 80:5000 --name syl_$1 syl/jobplus:$1