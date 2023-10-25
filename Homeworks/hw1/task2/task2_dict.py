for _ in range(int(input())):
    d = {chr(symb): 0 for symb in range(ord('A'), ord('Z') + 1)}
    
    _, K, line = input().split()
    
    for ch in filter(lambda ch: ch.isupper(), line):
        d[ch] += 1
    
    answ = [k for k, v in d.items() if v >= int(K)]
    
    print(*answ, sep = '')
        