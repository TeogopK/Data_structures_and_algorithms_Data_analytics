word = input()
N = int(input())
ch = input()

fc = N // len(word)
lc = N % len(word)
count = word.count(ch) * fc + word[:lc].count(ch)

print(count)