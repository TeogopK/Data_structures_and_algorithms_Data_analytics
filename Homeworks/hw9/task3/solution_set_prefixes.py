from collections import defaultdict

N = int(input())
fullnames = defaultdict(lambda: 1)
prefixes = set()

for i in range(N):
    name = input()
    
    if name in fullnames:
        print(name, fullnames[name])
    else:
        is_printed = False
        
        for i in range(len(name)):
            p = name[0:1+i]
            
            if not is_printed and p not in prefixes:
                print(p)
                is_printed = True
                
            prefixes.add(p)
        
        if not is_printed:
            print(name)
    
    fullnames[name] += 1
    