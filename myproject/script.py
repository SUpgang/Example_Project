from mypkg.hello import TestClass
from anotherpkg.stuff import AnotherTestClass
import sys

if __name__ == "__main__":
    myclass = TestClass(name="Me", unit_price=40)
    
    print(f'Main started')