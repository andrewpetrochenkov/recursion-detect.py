#!/usr/bin/env python
import recursion_detect


def recur():
    depth = recursion_detect.depth()
    print("depth = %s" % depth)
    if depth==10:
        return
    recur()

recur()
