# Install

## Clone The project
git clone --recursive git@github.com:mashhadbug/website.git

## Install Pelican in virtual envirnment
cd website
virtualenv .env
. .env/bin/activate
pip install pelican
pip install markdown

## Start Development Server
make devserver

## Push changes to github
make github
