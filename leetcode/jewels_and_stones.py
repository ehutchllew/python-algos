class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter: int = 0
        for i in range(len(S)):
            if S[i] in J:
                counter += 1
        return counter
