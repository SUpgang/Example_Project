# import own packages within project
from mypkg.hello import TestClass
from anotherpkg.stuff import AnotherTestClass

# unused import & ordering check
import sys

# package import
import pandas as pd

# Test for typing and unassigned variable
def my_function() -> str:
    x = 4
    return x, y


if __name__ == "__main__":

    print("Main started")

    # Change the following line and save. The on save formatting should be applied.
    dict_formatting = {"test": "formatter", "bla": "blubb"}

    myclass = TestClass(name="Me", unit_price=40)
    df = pd.DataFrame()

    # Linting error for f-string without variable
    print(f"Main ended.")
