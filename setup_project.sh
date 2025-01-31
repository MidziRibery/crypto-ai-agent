#!/bin/bash

# Create the project structure
mkdir -p backend/utils
touch backend/app.py backend/config.py backend/.env backend/firebase_key.json backend/requirements.txt
touch backend/utils/twitter_fetch.py backend/utils/summarize.py backend/utils/database.py

echo "Project structure created successfully."