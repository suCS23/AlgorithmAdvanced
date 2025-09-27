import time

def sort(list):
    
    s = time.perf_counter_ns()
    
    #Initialize a counter
    count = []
    for i in range (len(list)): count.append(0)
    
    #Compare elements and start counting
    for i in range (len(list)-1):
        for j in range (i+1,len(list)):
            if (list[i] < list [j]):
                count[j] += 1
            else:
                count[i] += 1
    
    #Initialize a sorted list
    sorted = []
    for i in range(len(list)) : sorted.append(0)

    #sort
    for i in range(len(list)) : sorted[count[i]] = list[i]

    print(f"\nAfter sorting: {sorted}")
    
    e = time.perf_counter_ns()
    print(f"Time taken to sort: {e-s} ns\n")
    
def sort_steps(list):
    
    #Initialize a counter
    count = []
    for i in range (len(list)): count.append(0)
    
    print('''\n====================================== 
=   Comparasions & counting loop:    =
======================================''')
    time.sleep(1)
    
    #Compare elements and start counting
    for i in range (len(list)-1):
        print(f"= Iteration i-{i} :                    =")
        time.sleep(1)
        for j in range (i+1,len(list)):
            if (list[i] < list [j]):
                count[j] += 1
            else:
                count[i] += 1
            
            print(f"= Iteration j-{j} : {count} =")
            time.sleep(1.5)
        print("=                                    =")       
    
    print("===============[ Done ]===============")
    print(f"\nFinal count list : {count}")   
    time.sleep(1)  
    
    #Initialize a sorted list
    sorted = []
    for i in range(len(list)) : sorted.append(0)
    
    print('''\n====================================== 
=             Sorting:               =
======================================''')
    time.sleep(1)
    #sort
    for i in range(len(list)) : 
        sorted[count[i]] = list[i]
        print(f"Iteration i-{i} : {sorted}")
        time.sleep(1.5)
    
    print("===============[ Done ]===============")
    print(f"\nAfter sorting : {sorted}\n")
    return sorted

sort([67,4,93,0,12,32])