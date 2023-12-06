from collections import defaultdict
class Solution:
    def encode_character(self, ch):
        if ch == 'A': return 0
        if ch == 'C': return 1
        if ch == 'G': return 2
        return 3

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        d = defaultdict(int)
        result = []
        hash_value = 0

        for i in range(9):
            hash_value = hash_value * 4 + self.encode_character(s[i])

        first_pow = 4 ** 9
        for i in range(9, len(s)):
            hash_value = hash_value * 4 + self.encode_character(s[i])
            d[hash_value] += 1

            if d[hash_value] == 2:
                result.append(s[i-9:i+1])

            hash_value -= first_pow * self.encode_character(s[i-9])

        return result
            