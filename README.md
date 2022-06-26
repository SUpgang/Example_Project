# Example_Project

A dummy project to test formatting, linting, project structure and imports within a minimal example.

## What I use
 - Windows 11 PC
 - Anaconda Navigator
 - VSCode

## Install packages for formatting and linting and type checking
Install linter Pylint then use Strg + Shift + P => Select Linter
```
pip install pylint
```
Install formatter black then go to settings => search Formatting => change Provider & format on save
```
pip install black 
```
Install type checker mypy
```
pip install mypy 
```

## Pylint
(Not used) Create rcfile for pylint
```Generate 
pylint --generate-rcfile > .pylintrc to create pylint file
```

## Pytest
Install pytest
```
pip install pytest 
```
create a tests directory with the same folder structure as the project. Create a test_*.py file to write tests for a module.

## Some References
https://code.visualstudio.com/docs/python/settings-reference
