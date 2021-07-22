index = 0
digits = '23'
path= ""
dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl",
       "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}


for i in range(index, len(digits)):
    print(i)
    for j in dic[digits[i]]:
        print(j)

