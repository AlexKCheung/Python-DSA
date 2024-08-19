def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # dictionary where key = sorted word, value = list of unsorted words
    word_dic = {}

    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word in word_dic:
            word_dic[sorted_word].append(word)
        else:
            word_dic[sorted_word] = [word]
    output = []
    for i in word_dic:
        output.append(word_dic[i])
    return output
