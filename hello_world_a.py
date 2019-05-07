#! /usr/bin/env python

from submodules_test_b import hello_world_b as b
from submodules_test_c import hello_world_c as c

def hello():
    print("Hello from submodule a")


if __name__ == "__main__":
    hello()
    b.hello()
    b.something_else()
    b.another_thing()
    c.hello()
    c.some_function()
    c.another_function()
    