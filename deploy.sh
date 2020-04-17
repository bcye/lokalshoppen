#!/bin/bash

eval "$(ssh-agent -s)" # Start ssh-agent cache
chmod 600 travis_rsa # Allow read access to the private key
ssh-add travis_rsa # Add the private key to SSH

git remote add deploy dokku@157.230.111.9:lokalshoppen
git push deploy dev

EOF