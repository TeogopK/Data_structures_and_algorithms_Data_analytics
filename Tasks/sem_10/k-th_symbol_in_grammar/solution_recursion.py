def find_char(level, idx):
    if level == 1:
        return '0'
    
    prev_char = find_char(level - 1, (idx + 1) // 2)
    num = int(prev_char) + 1
    binary_str = '01' if num == 1 else '10'

    return binary_str[(idx - 1) % 2]


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return int(find_char(n, k))
    