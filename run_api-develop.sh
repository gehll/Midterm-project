#!/user/bin/env bash

cd api
uvicorn main:bane --reload --host 0.0.0.0 --port 8000