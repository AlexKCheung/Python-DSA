def shipWithinDays(self, weights: List[int], days: int) -> int:
    # binary search to find the minimum capacity 
    # a linear search from 1 to sum(weights) + 1 only passes 78/88 testcases and time limit exceeded
    # create a function to check if a capacity works

    def check_capacity(capacity):
        if capacity < max(weights):
            return False
        current_ship = 0
        day_count = 1
        # print("CAPACITY CHECK:", capacity)
        for i in weights:
            # print(i, current_ship, day_count)
            if i + current_ship <= capacity:
                current_ship += i
            else:
                day_count += 1
                current_ship = i
            if day_count > days:
                return False
        return True
    
    left = 1
    right = sum(weights)
    while left <= right:
        middle = (left + right) // 2
        if not check_capacity(middle):
            left = middle + 1
        else:
            right = middle - 1
    return left
