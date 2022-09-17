#!/usr/bin/env python3

from distutils.debug import DEBUG
from test1 import Demo


class Demo2():
    def __init__(self):
        self.demo1 = Demo()
        self.Int1 = self.demo1.int1

    def run2(self):
        self.demo1.run()


if __name__ == "__main__":
    demo2 = Demo2()
    demo2.run2()



