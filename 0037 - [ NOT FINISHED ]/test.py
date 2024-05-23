pos = {i:[j for j in range(1,(i+1)%10)] for i in range(81)}

for j in range(81):
    print(pos[j])

for i in range(9):
    row = [item for arr in list(pos.values())[i*9:(i+1)*9] for item in arr]
    column = [item for key, arr in pos.items() if key % 9 == i for item in arr]    
    
    print(column)
