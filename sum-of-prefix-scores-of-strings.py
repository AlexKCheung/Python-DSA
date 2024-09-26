class Node:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def add_word(self, word):
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")
            if not cur.children[i]:
                cur.children[i] = Node()
            cur = cur.children[i]
            cur.count += 1

    def get_count(self, word):
        count = 0
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")
            cur = cur.children[i]
            count += cur.count
        return count

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        words_trie = Trie()

        for word in words:
            words_trie.add_word(word)

        output = []
        for word in words:
            output.append(words_trie.get_count(word))
        return output
