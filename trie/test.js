const Trie = require("./Trie").Trie;
const trie = new Trie();
const word_list = ["frodo", "front", "firefox", "fire"];
for (const word in word_list) {
	trie.insert(word_list[word]);
}

console.log(trie.search("friend"));
console.log(trie.search("frodo"));
console.log(trie.search("fire"));
console.log(trie.starts_with("fire"));
console.log(trie.starts_with("fro"));
console.log(trie.starts_with("jimmy"));
console.log(trie.starts_with("f"));
