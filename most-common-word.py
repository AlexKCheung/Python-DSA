def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    # as given in the constraints
    punctuation = ["!", "?", "'", ",", ";", "."]
    for i in paragraph:
        if i in punctuation:
            paragraph = paragraph.replace(i, " ")
    paragraph = paragraph.split(" ")

    counts = {}
    max_count = 0
    output_word = ""
    for i in paragraph:
        word = i.lower()
        if word != "" and word not in banned:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
            if counts[word] > max_count:
                max_count = counts[word]
                output_word = word

    return output_word