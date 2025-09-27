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
    
    print('''\n|====================================|
|   Comparasions & counting loop:    |
|====================================|''')
    time.sleep(1)
    
    #Compare elements and start counting
    
    print("| Compare two consecutive elements   |")
    print("| and increase the index of the      |")
    print("| largest in 'count' list            |")
    print("|                                    |")
    time.sleep(2)
    
    for i in range (len(list)-1):
        
        if (i == 1):
            print("| So on...                           |")
            
        print(f"| Iteration i-{i} :                    |")
        time.sleep(1)
        for j in range (i+1,len(list)):
            
            if(i == 0):
                print(f"| {list[i]} < {list[j]}?                           |")
                time.sleep(1)
                print(f"| {list[j]} is larger, index in list is {j}   |" if (list[i] < list[j]) else f"| {list[i]} is larger, index in list is {i}   |")
                time.sleep(1)
                print(f"| Therefor, increase count[{j}] by 1   |" if (list[i] < list[j]) else f"| Therefor, increase count[{i}] by 1   |")
                time.sleep(1)
                print("|                                    |")
                
            if (list[i] < list[j]):
                count[j] += 1
            else:
                count[i] += 1
            
            print(f"| Iteration j-{j} : {count} |")
            time.sleep(1.5)
        print("|                                    |")       
    
    print("|==============[ Done ]==============|")
    print(f"\nFinal count list : {count}")   
    time.sleep(1)  
    
    #Initialize a sorted list
    sorted = []
    for i in range(len(list)) : sorted.append(0)
    
    print('''\n|====================================| 
|             Sorting:               |
|====================================|''')
    time.sleep(1)
    print("| Using the 'count' list,            |")
    time.sleep(1)
    print("| the elements will be the new index |")
    print("| for our unsorted list              |")
    time.sleep(1)
    print("|                                    |")
    print("| It will be in a new list called    |")
    print("| 'Sorted'                           |")
    time.sleep(1)
    #sort
    for i in range(len(list)) : 
        
        if(i == 0):
                print("|                                    |")  
                print(f"| count[{i}] = {count[i]}                       |")
                time.sleep(1)
                print(f"| list[{i}] = {list[i]}                       |")
                time.sleep(1)
                print(f"| Therefor, sorted[{count[i]}] = {list[i]}          |")
                print("|                                    |") 
                time.sleep(1)
                
        sorted[count[i]] = list[i]
        print(f"| Iteration i-{i} : {sorted} |")
        time.sleep(1.5)
    
    print("|==============[ Done ]==============|")
    print(f"\nAfter sorting : {sorted}\n")

sort_steps([67,33,93,10,12,32])