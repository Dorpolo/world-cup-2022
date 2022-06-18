#!/bin/bash

HEROKU_TOKEN=$1

set -eu
wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh 5 | sh

echo heroku cli downloaded successfully

cat > ~/.netrc << EOF
machine api.heroku.com
login dorpolo@gmail.com
password $HEROKU_TOKEN
EOF
chmod 600 ~/.netrc
echo ~/.netrc updated successfully