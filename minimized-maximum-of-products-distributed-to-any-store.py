def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
    
    def max_products(products):
        cur_store = 0
        for i in quantities:
            cur_store += i // products
            if i % products > 0:
                cur_store += 1
            if cur_store > n:
                return False
        return True
    
    # for i in range(1, max(quantities)):
    #     if max_products(i):
    #         return i

    l = 1
    r = max(quantities)
    while l <= r:
        mid = (l + r) // 2
        if max_products(mid):
            r = mid - 1
        else:
            l = mid + 1
    return l
