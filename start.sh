#!/bin/bash

# Execute the gunicorn command
exec gunicorn --bind :${PORT:-10011} --workers ${WORKERS:-1} --threads ${THREADS:-4} --timeout 0 _server:app