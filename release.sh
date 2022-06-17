#!/bin/sh

# Adapted from https://toedter.com/2018/06/02/heroku-docker-deployment-update/

herokuAuthToken=$1
imageId=$(docker inspect registry.heroku.com/world-cup-22/web --format={{.Id}})
payload='{"updates":[{"type":"web","docker_image":"'"$imageId"'"}]}'

curl -n -X PATCH https://api.heroku.com/apps/world-cup-22/formation \
-d "$payload" \
-H "Content-Type: application/json" \
-H "Accept: application/vnd.heroku+json; version=3.docker-releases" \
-H "Authorization: Bearer $herokuAuthToken"