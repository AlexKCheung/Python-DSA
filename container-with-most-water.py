def maxArea(self, height: List[int]) -> int:
    cur_water = 0
    max_water = 0
    l, r = 0, len(height) - 1

    while l < r:
        cur_water = (r - l) * min(height[l], height[r])
        max_water = max(max_water, cur_water)
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1

    return max_water