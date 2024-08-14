
digits = ""
letters = {
    "2":"abc",
    "3":"def",
    "4":"ghi",
    "5":"jkl",
    "6":"mno",
    "7":"pqrs",
    "8":"tuv",
    "9":"wxyz",
}
l = 1
for digit in digits:
    l *= len(letters[digit])

sol = [""] * l if l > 1 else []

for i in range(l):
    r = l
    for j in range(len(digits)):
        s = letters[digits[j]]      # string
        r = r // len(s)             # remaining
        c = (i // r) % len(s)       # the character
        sol[i]+= s[c]
print(sol)