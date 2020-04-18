#!/bin/bash

eval "$(ssh-agent -s)" # Start ssh-agent cache
chmod 600 travis_rsa # Allow read access to the private key
ssh-add travis_rsa # Add the private key to SSH
ssh-keyscan -H api.bleiblokal.com >> ~/.ssh/known_hosts

git remote add deploy dokku@api.bleiblokal.com:lokalshoppen
git push deploy dev