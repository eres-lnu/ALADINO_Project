#! /bin/bash
while getopts w:p:n: flag
do
  # shellcheck disable=SC2220
  case "${flag}" in
     w) workshop=${OPTARG};;
     p) port=${OPTARG};;
     n) name=${OPTARG};;
  esac
done
if [ -z ${workshop+x} ]; then
  workshop=1
fi
if [ -z ${port+x} ]; then
  port=5000
fi
docker build -t backend_image .
if [ -z ${name+x} ]; then
  docker run --env WORKSHOP_NUM="${workshop}" -dp "${port}":5000 backend_image
else
  docker run --name "${name}" --env WORKSHOP_NUM="${workshop}" -dp "${port}":5000 backend_image
fi