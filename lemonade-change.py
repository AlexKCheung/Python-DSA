def lemonadeChange(self, bills: List[int]) -> bool:
    # don't need to keep track of 20's
    available_bills = {5: 0, 10: 0}
    for bill in bills:
        if bill == 5:
            available_bills[5] += 1
        if bill == 10:
            if available_bills[5] > 0:
                available_bills[5] -= 1
                available_bills[10] += 1
            else:
                return False
        if bill == 20:
            # want to give 10's first before the 5's
            if available_bills[10] > 0 and available_bills[5] > 0:
                available_bills[10] -= 1
                available_bills[5] -= 1
            elif available_bills[5] >= 3:
                available_bills[5] -= 3
            else:
                return False
    return True
