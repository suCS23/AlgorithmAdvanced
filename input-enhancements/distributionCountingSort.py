import time

def var1(list):
    
    s = time.perf_counter_ns()
    
    #Intialize an array for count 
    count = []
    for i in range (max(list)+1): count.append(0)

    #Count frequency for each element
    for i in range (len(list)): count[list[i]] += 1

    #Now calculate the start of their index
    for i in range (1,len(count)): count[i] += count[i-1]
    
    #Now start sorting
    sorted = []
    for i in range (len(list)): sorted.append(0)

    for i in range (len(list)): 
        sorted[count[list[i]]-1] = list [i]
        count[list[i]] -= 1
    
    e = time.perf_counter_ns()
    
    print(f"\nAfter sorting: {sorted}")
    print(f"Time taken to sort: {e-s} ns\n")

def var2(list):
    
    s = time.perf_counter_ns()
    
    maxi = max(list)
    mini = min(list)
    
    #Intialize an array for count 
    count = []
    for i in range (maxi - mini + 1): count.append(0)
    
    #Count frequency for each element
    for i in range (len(list)): count[list[i] - mini] += 1
    
    #Now calculate the start of their index
    for i in range (1,len(count)): count[i] += count[i-1]

    #Now start sorting
    sorted = []
    for i in range (len(list)): sorted.append(0)

    for i in range (len(list)): 
        sorted[count[list[i]-mini]-1] = list [i]
        count[list[i] - mini] -= 1
    
    e = time.perf_counter_ns()
    
    print(f"\nAfter sorting: {sorted}")
    print(f"Time taken to sort: {e-s} ns\n")
       
var2([13,11,12,13,12,12])