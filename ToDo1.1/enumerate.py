lst = [1, 2, 3, 4, 5]

enum = enumerate(lst, start=0) #start index parameter not required; default starts at index 0
for n in enum:
    ind = n[0]
    val = n[1]
    print(f"row: {ind}, val: {val}")
        
