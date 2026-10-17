def multiply(num1, num2):
    l1,l2=len(num1), len(num2)
        
    r,matrix="", [[0 for _ in range(l1+l2)] for _ in range(l1)]
    for i in range(l1):
        remainder=0
        for j in range(l2):
            t=int(num1[-1-i])*int(num2[-1-j])+remainder
            matrix[i][j+i]=t%10
            remainder=t//10
        if remainder:
            matrix[i][l2+i]=remainder
    
    print(matrix)
    remainder=0   
    for j in range(l1+l2):
        result=0
        for i in range(l1):
            result +=matrix[i][j]
        result+=remainder
        r=str(result%10)+r
        remainder=result // 10
        
    if remainder:
        r=str(remainder)+r
    return r

print(multiply("123", "456"))