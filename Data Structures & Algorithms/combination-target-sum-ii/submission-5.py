class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        out = []

        def f(cur, start, total):
            if total == target:
                out.append(cur.copy())
                return

            for i in range(start, n):
                # Skip duplicates at the same depth
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Prune impossible combinations
                if total + candidates[i] > target:
                    break

                cur.append(candidates[i])
                f(cur, i + 1, total + candidates[i])
                cur.pop()

        f([], 0, 0)
        return out