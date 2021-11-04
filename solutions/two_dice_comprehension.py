#!/usr/bin/env python3

def main():
    [print (f"({i},{j})") for i in range(1,6) for j in range (1,6) if i + j == 5 ]


if __name__ == "__main__":
    main()
