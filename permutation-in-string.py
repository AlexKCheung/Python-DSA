def is_permutation(self, cur_dict, cur_str):
    for i in cur_str:
        if i not in cur_dict:
            return False
        else:
            cur_dict[i] -= 1
            if cur_dict[i] == 0:
                del cur_dict[i]
    return True

def checkInclusion(self, s1: str, s2: str) -> bool:
    s1_dict = dict()
    for i in s1:
        if i in s1_dict:
            s1_dict[i] += 1
        else:
            s1_dict[i] = 1

    s1_len = len(s1)            

    for i in range(len(s2) - s1_len + 1):
        cur_dict = dict(s1_dict)
        cur_str = s2[i:i + s1_len]
        if self.is_permutation(cur_dict, cur_str):
            return True
    return False
