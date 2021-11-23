#! /bin/bash
while getopts n: flag
do
  # shellcheck disable=SC2220
  case "${flag}" in
     n) name=${OPTARG};;
  esac
done
if [ -z ${name+x} ]; then
  echo "Please insert a -n flag" >&2
  exit 1
fi
docker stop "${name}"
docker rm "${name}"
docker rmi backend_image