def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    output = []

    def dfs(index, target, path):
        if target < 0:
            return
        if target == 0:
            output.append(path)
            return
        for i in range(index, len(candidates)):
            dfs(i, target - candidates[i], path + [candidates[i]])

    dfs(0, target, [])
    return output