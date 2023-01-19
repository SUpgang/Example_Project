# import own packages within project
from mypackage.core.coremodule import call_hello
from mypackage.uipackage.uimodule import say_hello

# unused import & ordering check
import sys

if __name__ == "__main__":

    print("Script started")

    print(say_hello())
    call_hello()

    # Linting error for f-string without variable
    print(f"Script ended.")
