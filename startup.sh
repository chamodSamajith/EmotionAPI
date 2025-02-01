#!/bin/sh

# Install required Python dependencies
pip install --no-cache-dir -r /home/site/wwwroot/requirements.txt

# Start gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
