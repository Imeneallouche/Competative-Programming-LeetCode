
digits = "234"
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
length = 1
for digit in digits:
    length *= len(letters[digit])
print(length)

