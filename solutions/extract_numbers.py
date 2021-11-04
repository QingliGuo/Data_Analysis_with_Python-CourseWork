#!/usr/bin/env python3

def extract_numbers(s):
    items = s.split()
    new_items = []
    for item in items:
        try:
            new_items.append(int(item))
        except ValueError:
            try:
                new_items.append(float (item))
            except ValueError:
                pass
    return new_items

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
