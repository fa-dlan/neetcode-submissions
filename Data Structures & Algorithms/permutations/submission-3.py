class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        cur, rem = [[]], [nums]
        while rem[0]:
            new_cur, new_rem = [], []
            for i in range(len(cur)):
                for j in range(len(rem[i])):
                    new_cur.append(cur[i] + [rem[i][j]])
                    new_rem.append(rem[i][:j] + rem[i][j + 1:])
            cur, rem = new_cur, new_rem
        return cur