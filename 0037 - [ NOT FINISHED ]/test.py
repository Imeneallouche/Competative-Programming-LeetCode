pos = {i:[j for j in range(1,(i+1)%10)] for i in range(81)}

for j in range(9):
    print(pos[j])

for i in range(1):
    row1 = [item for arr in list(pos.values())[i*9:(i+1)*9] for item in arr]
    row2 = [item for arr in list(pos.values() if len(pos[i])!=1 else None)[i*9:(i+1)*9]  for item in arr]

    #column = [item for key, arr in pos.items() if key % 9 == i for item in arr]    
    
    print(row1)
    print(row2)
