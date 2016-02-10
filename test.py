import unittest
import sys
from StringIO import StringIO

from app import FizzBuzz

class TestSuite(unittest.TestCase):

    def test_one(self):
        app = FizzBuzz()
        for i in range(3, 100, 3):
            self.failIf(app.calc(i) != "Fizz" and app.calc(i) != "FizzBuzz")
        for i in range(5, 101, 5):
            self.failIf(app.calc(i) != "Buzz" and app.calc(i) != "FizzBuzz")
        for i in range(15, 101, 15):
            self.failIf(app.calc(i) != "FizzBuzz")


    def test_run(self):
        output = StringIO()

        app = FizzBuzz()
        app.run(100, output)

        self.failIf(len(output.getvalue().splitlines()) != 100)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
