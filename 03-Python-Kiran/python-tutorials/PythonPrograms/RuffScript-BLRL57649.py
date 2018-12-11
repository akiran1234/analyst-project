import re
import sys

import matplotlib.pyplot
x="hello this is stringhello hello iam hello"
y=x

words=re.findall('hell',x)  # to find
print(words)

mat=re.compile('hello')     # to find and replace
y=mat.sub('bolo',y)
print(y)

print(sys.implementation)

import numpy as np

