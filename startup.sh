#!/bin/sh

# Install missing dependencies
apt-get update
apt-get install -y libgl1 libgl1-mesa-glx libglib2.0-0 libsm6 libxext6 libxrender1

# Start gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
