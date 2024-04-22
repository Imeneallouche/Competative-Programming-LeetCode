s =input("ay go ay: ")
# f  g   d   d   g   f
# 0  1   2   3   4   5


# bafaa


# a   a   a   a
# 0   1   2   3
sub = ""
for i in range(len(s)):
    max = min(i, len(s)-i-1)
    pad = 1
    
    while pad<=max:
        o  = s[i-pad] == s[i + pad]
        e  = s[i-pad+1] == s[i+pad]

        if o:
            if len(sub)<2*pad+1: 
                sub = s[i-pad:i+pad+1]
            pad+=1

        elif e:
            if len(sub)<2*pad:
                sub = s[i-pad+1 : i+pad+1]
            pad+=1
        
        else:
            break 
                    
print(sub)