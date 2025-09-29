def stringMatchingBruteForce(text, pattern):
    indices = []
    
    for i in range (len(text) - len(pattern) + 1):
        j = 0
        
        while j < len(pattern) and pattern [j] == text[i+j]:
            j += 1
            
        if j == len(pattern):
            indices.append(i)
        
    return indices if len(indices) != 0 else -1

print(stringMatchingBruteForce("Hello saud saud saud", "saud"))