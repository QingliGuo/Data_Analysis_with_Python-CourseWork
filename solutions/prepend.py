#!/usr/bin/env python3

class Prepend(object):
    def __init__(self,pram1):
        self.pre = pram1

    def write(self, pram):
        print (f'{self.pre}{pram}')
    # Add the methods of the class here

def main():
    p = Prepend("+++ ")
    p.write("Hello")

if __name__ == "__main__":
    main()
