import pickle

import pandas as pd
import numpy as np
import sys

#定义函数
def power(base, index, **kwargs):
    result = int(base)
    for i in range(1, int(index)):
        result =  result*int(base)
    return result

if __name__ == "__main__":
    a = sys.argv[1]
    n = sys.argv[2]
    print(power(a,n))