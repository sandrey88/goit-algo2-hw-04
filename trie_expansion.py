from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern: str) -> int:
        """
        Підраховує кількість слів у дереві, які закінчуються на заданий шаблон.
        
        Args:
            pattern (str): Шаблон суфіксу для пошуку
            
        Returns:
            int: Кількість слів, що закінчуються на заданий шаблон
            
        Raises:
            TypeError: Якщо pattern не є рядком
        """
        if not isinstance(pattern, str):
            raise TypeError("Pattern повинен бути рядком")
        
        # Ефективний обхід Trie без створення всіх слів
        def dfs(node, path, pattern):
            cnt = 0
            if node.value is not None:
                word = ''.join(path)
                if word.endswith(pattern):
                    cnt += 1
            for char, child in node.children.items():
                path.append(char)
                cnt += dfs(child, path, pattern)
                path.pop()
            return cnt
        
        return dfs(self.root, [], pattern)
    
    def has_prefix(self, prefix: str) -> bool:
        """
        Перевіряє, чи існують слова з заданим префіксом у дереві.
        
        Args:
            prefix (str): Префікс для пошуку
            
        Returns:
            bool: True, якщо існує хоча б одне слово з таким префіксом, інакше False
            
        Raises:
            TypeError: Якщо prefix не є рядком
        """
        if not isinstance(prefix, str):
            raise TypeError("Prefix повинен бути рядком")
        
        # Використовуємо метод keys_with_prefix з базового класу
        # Якщо список не порожній, то префікс існує
        return len(self.keys_with_prefix(prefix)) > 0

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat
