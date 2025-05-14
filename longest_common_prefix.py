from trie import Trie

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        # Перевірка на коректність вхідних даних
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            return ""
        if not strings:
            return ""
        # Вставляємо всі слова у Trie
        for i, word in enumerate(strings):
            self.put(word, i)
        # Пошук найдовшого спільного префікса
        prefix = []
        node = self.root
        while True:
            # Якщо вузол має більше одного нащадка або це кінець слова — зупиняємось
            if len(node.children) != 1 or node.value is not None:
                break
            char = next(iter(node.children))
            prefix.append(char)
            node = node.children[char]
        return ''.join(prefix)

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
