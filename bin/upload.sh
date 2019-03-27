#!/usr/bin/env bash
rm dist/ -rf
rm build/ -rf
python setup.py sdist bdist_wheel
python -m twine upload dist/*
