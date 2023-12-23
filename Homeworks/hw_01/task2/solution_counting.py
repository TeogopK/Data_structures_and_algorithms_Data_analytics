for _ in range(int(input())):
    v = [0] * 256
    
    _, K, line = input().split()
    
    for ch in line:
        v[ord(ch)] += 1
    
    answ = [chr(n) for n in range(ord('A'), ord('Z') + 1) if v[n] >= int(K)]
    
    print(*answ, sep = '')