#!/usr/bin/env python3

def acronyms(s):
    acronyms_list = []

    Str = s.split()
    
    for string in Str:

        while not string[0].isalnum() and len(string)>1:    ## remove punctuation in the beginning of the string
            string  = string.strip (string[0])
        
        while not string[-1].isalnum() and len(string) > 1:     ## remove punctuation in the end of the string
            string = string.strip (string[-1])

        if string.isupper() and len(string)>1:
            acronyms_list.append (string)

    return acronyms_list

def main():
    
    print(acronyms("""For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."""))


if __name__ == "__main__":
    main()
