#!/usr/bin/env python3


def main():
#    pass
    for row in range (10):
        row += 1
        for column in range (10):
            column += 1

            if column == 10:
                print ('{:>4d}'.format(row * column))
            else:
                print ('{:>4d}'.format(row * column), end = "")

if __name__ == "__main__":
    main()
