def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
    # find count of each number
    # create a list of pairs (number, count)
    # sort list by key lambda x: count
    # remove the first k elements
    # count unique elements
    counts_dict = {}
    for i in arr:
        if i in counts_dict:
            counts_dict[i] += 1
        else:
            counts_dict[i] = 1
    counts_list = []
    for i in counts_dict:
        counts_list.append([i, counts_dict[i]])
    
    counts_list.sort(key = lambda x: x[1])

    while k > 0:
        k -= 1
        counts_list[0][1] -= 1
        if counts_list[0][1] == 0:
            counts_list.remove(counts_list[0])

    return len(counts_list)


