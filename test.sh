#!/bin/bash
python -m unittest discover -s src
rm -rf src/__pycache__/*
