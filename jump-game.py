def canJump(self, nums: List[int]) -> bool:
    jump_left = 0
    for i in nums:
        if jump_left < 0:
            return False
        jump_left = max(jump_left, i) - 1
    return True