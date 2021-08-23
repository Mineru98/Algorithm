# -*- coding:utf-8 -*-
from Trie import Trie

trie = Trie()
word_list = ["frodo", "front", "firefox", "fire"]
for word in word_list:
    trie.insert(word)

print(trie.search("friend"))
print(trie.search("frodo"))
print(trie.search("fire"))
print(trie.starts_with("fire"))
print(trie.starts_with("fro"))
print(trie.starts_with("jimmy"))
print(trie.starts_with("f"))