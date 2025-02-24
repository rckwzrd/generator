#!/bin/bash
python src/main.py
rm -rf src/__pycache__/*
cd public && python3 -m http.server 8888 
