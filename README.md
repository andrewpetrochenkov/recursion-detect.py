<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/recursion-detect.svg?maxAge=3600)](https://pypi.org/project/recursion-detect/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/recursion-detect.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/recursion-detect.py/actions)

### Installation
```bash
$ [sudo] pip install recursion-detect
```

#### Examples
```python
>>> import recursion_detect
>>> def recur():
    depth = recursion_detect.depth()
    print("depth = %s" % depth)
    if depth==5:
        return
    recur()

>>> recur()
0
1
2
3
4
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
