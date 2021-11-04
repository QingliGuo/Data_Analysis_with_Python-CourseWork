#!/usr/bin/env python3

def distinct_characters(L):
    dist_letter = {}
    for word in L:
        word_set = set(list(word))
        dist_letter[word] = len(word_set)
    return dist_letter

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
