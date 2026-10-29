class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []
        def solve(start, target):
            if target == 0:
                ans.append(path.copy())
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                solve(i + 1, target - candidates[i])
                path.pop()

        solve(0, target)
        return ans