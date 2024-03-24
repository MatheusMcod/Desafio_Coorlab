#!/bin/bash

cd backend
pip install -r requirements.txt
python3 main.py &

cd ..

cd frontend
npm install
npm run dev



