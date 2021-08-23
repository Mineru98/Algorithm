class Node {
	constructor(key, data = null) {
		this.key = key;
		this.data = data;
		this.children = {};
	}
}

class Trie {
	constructor() {
		this.head = new Node(null);
	}

	insert(string) {
		let current_node = this.head;
		for (const char in string) {
			if (!current_node.children.hasOwnProperty(string[char])) {
				current_node.children[string[char]] = new Node(string[char]);
			}
			current_node = current_node.children[string[char]];
		}
		current_node.data = string;
	}

	search(string) {
		let current_node = this.head;

		for (const char in string) {
			if (current_node.children.hasOwnProperty(string[char])) {
				current_node = current_node.children[string[char]];
			} else {
				return false;
			}
		}

		if (current_node.data) {
			return true;
		} else {
			return false;
		}
	}

	starts_with(prefix) {
		let current_node = this.head;
		let words = [];

		for (const p in prefix) {
			if (current_node.children.hasOwnProperty(prefix[p])) {
				current_node = current_node.children[prefix[p]];
			} else {
				return null;
			}
		}

		current_node = [current_node];
		let next_node = [];
		while (true) {
			for (const node in current_node) {
				if (current_node[node].data) {
					words.push(current_node[node].data);
				}
				next_node = next_node.concat(Object.values(current_node[node].children));
			}

			if (next_node.length !== 0) {
				current_node = next_node;
				next_node = [];
			} else {
				break;
			}
		}

		return words;
	}
}

exports.Trie = Trie;
