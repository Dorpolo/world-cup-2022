#!/bin/bash

HEROKU_TOKEN=$1
HEROKU_APP_NAME=world-cup-22

set -eu
wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh 5 | sh
cat > ~/.netrc << EOF
machine api.heroku.com
login dorpolo
password $HEROKU_TOKEN
EOF
chmod 600 ~/.netrc