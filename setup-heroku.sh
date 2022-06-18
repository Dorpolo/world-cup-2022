#!/bin/bash

HEROKU_TOKEN=$1

echo Writing permissons into ~/.netrc

cat > ~/.netrc << EOF
machine api.heroku.com
  login dorpolo@gmail.com
  password $HEROKU_TOKEN
machine git.heroku.com
  login dorpolo@gmail.com
  password $HEROKU_TOKEN
EOF
chmod 600 ~/.netrc
cat ~/.netrc
echo ~/.netrc updated successfully