import string
import time

def shiftingTable(pattern):
    
    m = len(pattern)
    alphabet = {letter: m for letter in string.ascii_uppercase}
    alphabet[' '] = m
    
    for i in range(m-1):
        alphabet[pattern[i]] = m - 1 - i
        
    return alphabet

def horspool(text, pattern):

    text, pattern = text.upper(), pattern.upper()
    alphabet = shiftingTable(pattern)
    n, m = len(text), len(pattern)
    
    i = m-1
    
    while i < n: 
        k = 0

        while m > k and text[i-k] == pattern [m-1-k]:
            k += 1
            if (k == m): 
                return i - m + 1
        
        i += alphabet[text[i]]

    return -1
            
text = "Hello sd au ds aud sa dhsuiagdieu dhsakgs sgyauketyu saud alfhaid"   
print(horspool(text, "saud"))