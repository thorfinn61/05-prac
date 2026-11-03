def word_ladder(start: str, end: str, sentence: list[str]) -> int:
    words = set(sentence)
    if end not in words:
        return 0
    letters = set("".join(sentence))
    words.discard(start)
    queue = [(start,1)]
    for word, length in queue:
        if word == end:
            return length
        for i in range(len(word)):
            for letter in letters:
                nxt = word[:i] + letter + word[i + 1:]
                if nxt in words:
                    words.remove(nxt)
                    queue.append((nxt, length + 1))
    return 0

if __name__ == "__main__":
    print(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
    print(word_ladder("a", "c", ["a", "b", "c"]))