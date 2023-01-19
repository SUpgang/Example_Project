# Example_Project

A dummy project to test formatting, linting, project structure and imports within a minimal example.

## What I use
 - Windows 11 PC
 - Miniconda
 - VSCode

# Setup
## Environment
  1. Create a new virtual environment through conda
```
    conda create -n myenv python=3.11
```
  2. Activate the environment to install packages through pip
```
    conda activate myenv
```
  3. Select interpreter in vscode CTRL + Shift + P: Select Interpreter

## Linting, formatting and type checking
  1. Install linting, formatting and type checking through requirements.txt
```
  pip install -r requirements.txt
```
  2. or manually 
```
  pip install pylint black mypy
```
  3. Select linter through CTRL + Shift + P: Select Linter
  4. or manuall through ```settings.json```
```
    {
     "python.linting.enabled": true,
     "python.linting.pylintEnabled": true,
     "python.linting.mypyEnabled": true,
    }
```
## Imports
Within the package for all ```*.py``` which will not be executed, use relative imports where ```.module``` searches in the current folder for ```module``` and ```..module``` moves one directory up and searches for ```module```. On the top level of the package you can insert a ```main.py``` with absolute imports. The package is found if installed properly through pip.

## Install package
Install the package in develop mode by using
```
pip install -e .
```

## (Not needed) Fix pylint import errors
  1. Create pylintrc through 
```
    pylint --generate-rcfile >.pylintrc
```
  2. Add 
```
    init-hook='import sys; sys.path.append(".")'
```

## Pytest
  1. Install pytest
```
    pip install pytest 
```
  2. Create a ```tests``` directory with the same folder structure as the project. For each file in your package, create a test_X.py file to write tests for a module X.
  3. Enable pytest in Vscode through CTRL + Shift + P: Configure Tests and choose pytest and the tests directory
  4. or manually through the ```settings.json```
```
    {
     "python.testing.pytestArgs": ["tests"],
     "python.testing.unittestEnabled": false,
     "python.testing.pytestEnabled": true
    }
```

# References
  - https://code.visualstudio.com/docs/python/settings-reference
