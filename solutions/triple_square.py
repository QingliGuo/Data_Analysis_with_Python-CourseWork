#!/usr/bin/env python3

def triple (x):
    return x * 3
def square (x):
    return x ** 2

def main():
#    pass
    for i in range (1,11):
        tri = triple (i)
        squ = square (i)

        if squ > tri:
            break

        print (f"triple({i})=={tri} square({i})=={squ}")


if __name__ == "__main__":
    main()
