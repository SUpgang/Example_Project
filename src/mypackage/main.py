# import own packages within project
from mypackage.core.coremodule import call_hello
from mypackage.uipackage.uimodule import say_hello

# unused import & ordering check
import sys
import time

if __name__ == "__main__":

    print("Main started")

    print(say_hello())
    call_hello()
    time.sleep(30)
    # Linting error for f-string without variable
    print(f"Main ended")
