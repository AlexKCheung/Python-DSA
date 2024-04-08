def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
    sum = 0
    str_x = str(x)
    for i in range(len(str_x)):
        sum += int(str_x[i])
    if x % sum == 0:
        return sum
    return -1