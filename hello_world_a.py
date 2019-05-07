#! /usr/bin/env python

from submodules_test_b import hello_world_b as b

def hello():
    print("Hello from submodule a")


if __name__ == "__main__":
    hello()
    b.hello()
    