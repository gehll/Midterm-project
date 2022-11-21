#!/usr/bin/env bash

echo "Running API in the port $PORT"

uvicorn main:bane --host 0.0.0.0 --port $PORT
