#!/usr/bin/env python3

class Rational(object):
    def __hash__ (self, pram1,pram2):
        self = pram1/pram2
def merge(*lst):
    data = []
    for i in lst:
        data += i
    min_point = min(data)
    max_point = max(data)

    elements = list(range(min_point, max_point+1))
    new_data = []
    for element in elements:
        if data.count(element) != 0:
            new_data.append(element)
    print (new_data)

def main():
    merge([1,4],[3,8])

if __name__ == "__main__":
    main()
