class Weight:
    def __init__(self, r, t, idx):
        self.idx = idx
        self.r = r
        self.t = t
        
    def __lt__(self, other):
        if self.r ** 2 / self.t == other.r ** 2 / other.t:
            return self.r > other.r
        return self.r ** 2 / self.t > other.r ** 2 / other.t
    
    def __repr__(self):
        return f"{self.idx}"
    
weights = []

n = int(input())

for i in range(n):
    in_ = input().split()
    d, t = in_[0], in_[1]
    weights.append(Weight(int(d) / 2, int(t), i + 1))


weights.sort()

print(' '.join([str(weight.idx) for weight in weights]))