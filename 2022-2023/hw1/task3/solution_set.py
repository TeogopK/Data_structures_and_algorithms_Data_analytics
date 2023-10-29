n = int(input())

sold = set(map(int, input().split()))

# because there can be 1M concecutive numbers so Ivan will be 1M + 1
# range() function is also exclusive,
# range(10) will produce numbers 0, 1, 2 ... 8, 9

for i in range(1, 1_000_002): 
    if i not in sold:
        print(i)
        break