s = int(input("Qiw: "))

r = s if -5<s<5 else (int(s>0) - int(s<0))*2*2 - (s>0)

print(r)