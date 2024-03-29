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
		for (const char of string) {
			if (!current_node.children.hasOwnProperty(char)) {
				current_node.children[char] = new Node(char);
			}
			current_node = current_node.children[char];
		}
		current_node.data = string;
	}

	search(string) {
		let current_node = this.head;

		for (const char of string) {
			if (current_node.children.hasOwnProperty(char)) {
				current_node = current_node.children[char];
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

		for (const p of prefix) {
			if (current_node.children.hasOwnProperty(p)) {
				current_node = current_node.children[p];
			} else {
				return null;
			}
		}

		let current_node_list = [current_node];
		let next_node = [];
		while (true) {
			for (const node of current_node_list) {
				if (node.data) {
					words.push(node.data);
				}
				next_node = next_node.concat(Object.values(node.children));
			}

			if (next_node.length !== 0) {
				current_node_list = next_node;
				next_node = [];
			} else {
				break;
			}
		}

		return words;
	}
}

exports.Trie = Trie;
