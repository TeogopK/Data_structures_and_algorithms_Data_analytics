MAX_RESULT = 1_000_001
n = int(input())

sold = list(map(int, input().split()))

placeholder = [0] * (MAX_RESULT + 1) # position 0 will always be empty

for ticket in sold:
    if ticket > 0 and ticket < MAX_RESULT:
        placeholder[ticket] = 1
    
for i in range(1, MAX_RESULT + 1):
    if placeholder[i] != 1:
        print(i)
        break