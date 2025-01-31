#!/bin/bash

echo "🚀 Setting up React Frontend..."

# Step 1: Create frontend directory
mkdir frontend && cd frontend

# Step 2: Initialize React App
npx create-react-app . --use-npm

# Step 3: Install dependencies
npm install axios firebase tailwindcss react-router-dom

# Step 4: Create folders & files
mkdir -p src/components src/pages src/services src/assets
touch src/firebase.js src/config.js .env README.md tailwind.config.js

echo "✅ Frontend setup complete!"
echo "Next: cd frontend && npm start to run the project!"
