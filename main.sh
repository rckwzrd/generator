#!/bin/bash
python src/main.py
rm -rf src/__pycache__/*
cd docs && python3 -m http.server 8888 
