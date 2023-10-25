# Note this solution will not pass all tests
input()

arr = sorted(input())

digits = [i for i in arr if i.isdigit()]
lowers = [i for i in arr if i.islower()]
uppers = [i for i in arr if i.isupper()]

result = digits + lowers + uppers

print(*result, sep = '')