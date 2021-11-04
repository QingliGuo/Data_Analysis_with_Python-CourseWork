#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):

    fcol = np.arange (n).reshape(n,1)
    result = fcol * np.arange(n)
    return result

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()