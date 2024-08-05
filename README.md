# Example_Project

A sample project providing a basic structure, logging functionality and demonstrating fixes for some annoying pitfalls.

For linting, type checking and formatting the project uses
 - black
 - pylint
 - mypy

## Imports
Relative imports can be used if the ```moduleA.py``` file is executed with the command
```
python -m mypackage.moduleA
```
The script can be used if the package was installed in develop mode by using
```
pip install -e .
```
A requirement for this is to setup the toml file correctly.

## Further linting settings
  1. Create pylintrc through 
```
    pylint --generate-rcfile >.pylintrc
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
  5. If the package is installed in developer mode the test will find the imports and run well.

## Export as executable
 1. Install pyinstaller
```
  pip install pyinstaller
```
 2. Export the project by calling
```
  pyinstaller --path=.\ -F .\src\mypackage\main.py
  pyinstaller --path=.\ -F .\script\script.py
```

# References
  - https://code.visualstudio.com/docs/python/settings-reference
