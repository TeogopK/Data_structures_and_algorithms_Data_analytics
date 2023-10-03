# Separating the given values in two containers by even/ odd

N = int(input())

odd = []
even = []

for _ in range(N):
    a = int(input())
    
    if(a % 2 == 0):
        even.append(a)
    else:
        odd.append(a)

for el in even:
    print(el)
    
for el in odd:
    print(el)