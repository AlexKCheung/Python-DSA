def gcdOfStrings(self, str1: str, str2: str) -> str:

    # corner case? 
    if str1 + str2 != str2 + str1:
        return ""

    # assume and make str1 to be longer than str2
    if len(str1) > len(str2):
        pass
    else:
        str1, str2 = str2, str1
    original_len_str2 = len(str2)

    # while str2: check if it divides str1
    while len(str2) > 0:
        multiplier = int(len(str1) / len(str2))
        if str1 == str2 * multiplier:
            test_1 = original_len_str2 / len(str2)
            if test_1 == int(test_1):
                return str2
        str2 = str2[:-1]
    return ""
    