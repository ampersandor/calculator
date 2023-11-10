#!/bin/bash

python3.10 -m venv docs/.venv
source docs/.venv/bin/activate

./setup.sh

cd docs

pip3 install -r requirements.txt

make clean && make html
