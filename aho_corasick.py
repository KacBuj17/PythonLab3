from collections import deque, defaultdict

class AhoCorasick:
    def __init__(self):
        self.trie = {0: {}}
        self.fail = {}
        self.output = defaultdict(list)
        self.state_count = 0

    def add_pattern(self, input_pattern):
        state = 0
        for char in input_pattern:
            if char not in self.trie[state]:
                self.state_count += 1
                self.trie[state][char] = self.state_count
                self.trie[self.state_count] = {}
            state = self.trie[state][char]
        self.output[state].append(input_pattern)

    def build(self):
        queue = deque()
        for char, next_state in self.trie[0].items():
            self.fail[next_state] = 0
            queue.append(next_state)
        while queue:
            state = queue.popleft()
            for char, next_state in self.trie[state].items():
                fail_state = self.fail[state]
                while fail_state and char not in self.trie[fail_state]:
                    fail_state = self.fail[fail_state]
                self.fail[next_state] = self.trie[fail_state].get(char, 0)
                self.output[next_state].extend(self.output[self.fail[next_state]])
                queue.append(next_state)

    def search(self, input_text):
        state = 0
        results = []
        for i, char in enumerate(input_text):
            while state and char not in self.trie[state]:
                state = self.fail[state]
            state = self.trie[state].get(char, 0)
            results.extend((i - len(pattern) + 1, pattern) for pattern in self.output[state])
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
