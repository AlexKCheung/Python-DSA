def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # for each word, use the sorted of that word as the key 
    # use key in dictionary of lists
    # use values to make output
    anagram_dict = {}
    for i in strs:
        # sorted(i) returns list, so we combine it to a string
        cur_word = "".join(sorted(i))
        if cur_word in anagram_dict:
            anagram_dict[cur_word].append(i)
        else:
            anagram_dict[cur_word] = [i]

    output_list = []
    for i in anagram_dict:
        output_list.append(anagram_dict[i])

    return output_list
