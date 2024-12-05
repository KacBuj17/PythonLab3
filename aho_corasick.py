from collections import deque, defaultdict


class AhoCorasick:
    def __init__(self):
        self.trie = {}
        self.fail = {}
        self.output = defaultdict(list)
        self.state_count = 0

    def add_pattern(self, input_pattern):
        state = 0
        for char in input_pattern:
            if char not in self.trie.get(state, {}):
                self.trie.setdefault(state, {})[char] = self.state_count + 1
                self.state_count += 1
            state = self.trie[state][char]
        self.output[state].append(input_pattern)

    def build(self):
        queue = deque()
        for char, next_state in self.trie.get(0, {}).items():
            self.fail[next_state] = 0
            queue.append(next_state)
        while queue:
            state = queue.popleft()
            for char, next_state in self.trie.get(state, {}).items():
                queue.append(next_state)
                fail_state = self.fail.get(state, 0)
                while fail_state and char not in self.trie.get(fail_state, {}):
                    fail_state = self.fail.get(fail_state, 0)
                self.fail[next_state] = self.trie.get(fail_state, {}).get(char, 0)
                self.output[next_state].extend(self.output[self.fail[next_state]])

    def search(self, input_text):
        state = 0
        results = []
        for i, char in enumerate(input_text):
            while state and char not in self.trie.get(state, {}):
                state = self.fail[state]
            state = self.trie.get(state, {}).get(char, 0)
            if self.output[state]:
                for pattern in self.output[state]:
                    results.append((i - len(pattern) + 1, pattern))
        return results


if __name__ == "__main__":
    aho = AhoCorasick()

    words = ["quick", "fox", "dog", "bark", "lazy"]

    for word in words:
        aho.add_pattern(word)

    aho.build()

    text = "the quick brown fox jumps over the lazy dog while the dog barks at the fox"

    matches = aho.search(text)

    print(matches)
