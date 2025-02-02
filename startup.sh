#!/bin/sh

# Log the start of deployment
echo "Starting deployment..." > /home/site/wwwroot/startup.log

# Install required Python dependencies
pip install --no-cache-dir -r /home/site/wwwroot/requirements.txt >> /home/site/wwwroot/startup.log 2>&1

# Start gunicorn server
gunicorn -w 4 -b 0.0.0.0:8000 app:app >> /home/site/wwwroot/startup.log 2>&1
