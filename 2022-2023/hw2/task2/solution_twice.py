N = int(input())

names = [input() for _ in range(N)]
scores = [(name, int(input())) for name in names]

scores.sort(key = lambda score: score[0])
scores.sort(key = lambda score: score[1], reverse = True)

for score in scores:
    print(*score)