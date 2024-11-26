class State:
    def __init__(self, name, output):
        self.name = name
        self.output = output
        self.transitions = {}

    def add_transition(self, input_symbol, next_state):
        self.transitions[input_symbol] = next_state

    def next_state(self, input_symbol):
        return self.transitions.get(input_symbol)


class MooreMachine:
    def __init__(self):
        self.states = {}
        self.current_state = None

    def add_state(self, state):
        self.states[state.name] = state
        if self.current_state is None:
            self.current_state = state

    def set_initial_state(self, state_name):
        self.current_state = self.states.get(state_name)

    def process_input(self, input_sequence):
        outputs = []
        for symbol in input_sequence:
            outputs.append(self.current_state.output)
            next_state = self.current_state.next_state(symbol)
            if next_state is None:
                raise ValueError(f"Brak przejścia dla symbolu {symbol} w stanie {self.current_state.name}")
            self.current_state = next_state
        outputs.append(self.current_state.output)
        return outputs


if __name__ == "__main__":
    s1 = State("S1", "Output1")
    s2 = State("S2", "Output2")
    s3 = State("S3", "Output3")

    s1.add_transition(0, s2)
    s1.add_transition(1, s3)
    s2.add_transition(0, s1)
    s2.add_transition(1, s3)
    s3.add_transition(0, s2)
    s3.add_transition(1, s1)

    machine = MooreMachine()
    machine.add_state(s1)
    machine.add_state(s2)
    machine.add_state(s3)

    machine.set_initial_state("S1")

    input_sequence = [0, 1, 0, 0, 1]
    outputs = machine.process_input(input_sequence)

    print("Sekwencja wyjściowa:", outputs)
