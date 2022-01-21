# Introduction
This project is a Tic Tac Toe game based on a python based console application.

# Prerequisites
* python 3.9.x

# Virtual Environment Setup
## Activate
```bash
python3.9 -m venv venv
source venv/bin/activate
```
## Verify venv Operation
```bash
$ python --version
Python 3.9.7
$ pip --version
pip 21.2.4 from /Users/user/repos/se_practice/tic-tac-toe/venv/lib/python3.9/site-packages/pip (python 3.9)
```

## Install Required Packages
```bash
pip install -r install.txt
```

## Deactivate
```bash
deactivate
```

# Testing
Note: venv must be running to run pytest using the proper version of python
```bash
python -m pytest -vv
```

# Starting the game
python -m tic_tac_toe
