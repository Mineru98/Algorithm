interface INode {
	key?: string;
	data?: string;
}

class Node {
	public key: string;
	public data: string;
	public children: INode;

	constructor(key: string, data: string = null) {
		this.key = key;
		this.data = data;
		this.children = {};
	}
}

export class Trie {
	private head: Node;
	constructor() {
		this.head = new Node(null);
	}

	insert(str: string) {
		let current_node: Node = this.head;
		for (const char of str) {
			if (!current_node.children.hasOwnProperty(char)) {
				current_node.children[char] = new Node(char);
			}
			current_node = current_node.children[char];
		}
		current_node.data = str;
	}

	search(str: string) {
		let current_node = this.head;

		for (const char of str) {
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

	starts_with(prefix: string) {
		let current_node: Node = this.head;
		let words = [];

		for (const p of prefix) {
			if (current_node.children.hasOwnProperty(p)) {
				current_node = current_node.children[p];
			} else {
				return null;
			}
		}

		let current_node_list: Node[] = [current_node];
		let next_node: Node[] = [];
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
