#!/usr/bin/env python3

def word_frequencies(filename = 'src/alice.txt'):
    
    word_freq = {}
    
    f = open (filename, "r")

    for line in f.readlines():
        
        line = line.strip ()
        
        words = line.split()
        words = [word.strip("""!"#$%&'()*,-./:;?@[]_""") for word in words]  ## remove the punctuation of the word
        
        if len(words) >= 1:        ## only count those with word(s)
            
            for word in words:
                if word in word_freq:                    
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1
        else:
            continue

    f.close()

    return word_freq

def main():
    
    word_freqency = word_frequencies(filename = 'src/alice.txt')

    for key,value in word_freqency.items():
        print (f'{key}\t{value}')

if __name__ == "__main__":
    main()
