#!/usr/bin/env bash

APP_NAME="core-midterm"

# Login to Heroku container registry
heroku container:login

# Build and upload to Heroku

heroku container:push --app $APP_NAME web

# Run the image container in Heroku

heroku container:release --app $APP_NAME web