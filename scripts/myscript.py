"""Script outside of package to test imports """

import time

from mypackage.subpackage.submodule1 import say_hello
from mypackage.module1 import say_bye


if __name__ == "__main__":

    print("Script started")

    print(say_hello())
    print(say_bye())
    time.sleep(3)

    print("Script ended.")
