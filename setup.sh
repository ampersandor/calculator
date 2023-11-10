#!/bin/bash

pip3 install --upgrade pip
pip3 install --upgrade build

python3 -m build

pip3 install dist/calculator-0.0.1.tar.gz
