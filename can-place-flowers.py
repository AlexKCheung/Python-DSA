def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    planted = 0
    # 2 means we know it has a neighboring plant

    # if one flower only 
    if len(flowerbed) == 1 and flowerbed[0] == 0:
        flowerbed[0] = 1
        planted += 1
    # first and last
    if len(flowerbed) > 1 and flowerbed[0] == 0 and flowerbed[1] != 1:
        flowerbed[0] = 1
        flowerbed[1] = 2
        planted += 1
    if len(flowerbed) > 1 and flowerbed[-1] == 0 and flowerbed[-2] != 1:
        flowerbed[-1] = 1
        flowerbed[-2] = 2
        planted += 1

    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i] == 1 or flowerbed[i] == 2:
            continue
        # if flowerbed[i - 1] != 0 or flowerbed[i + 1] != 0:
        #     continue
        if flowerbed[i - 1] == 1 or flowerbed[i + 1] == 1:
            continue
        # else
        flowerbed[i] = 1
        flowerbed[i+1] = 2
        planted += 1

    print(planted, flowerbed)
    if planted >= n:
        return True
    return False