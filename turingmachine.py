"""This is the Turing Machine Module it has the turing machine class and program"""


class TM:
    """This class is the turing machine class it initiates here"""
    def __init__(self):
        self.state = None
        self.program = {}

    def read(self, program):
        """This method reads in and stores into memory the turing machines PROGRAM"""
        for line in program.splitlines():
            if line:
                state, symbol, next_state, write, direction = line.split(' ')
                self.program[state, symbol] = (next_state, write, direction)

    def execute(self, tape, tape_pos, start, final, reject):
        """This method executes the turing machine on the currently read program and the tape
        inserted as the tape variable """
        count = 0
        tape_list = list(tape)
        current_value = tape_list[tape_pos]
        self.state = start
        intial_instructions = self.program[self.state, current_value]
        printer = ' ' * tape_pos
        print("STEP: " + str(count) + " STATE: "+intial_instructions[0])
        print("POS:  "+printer + '*')
        print("TAPE: "+tape)
        while self.state != reject and self.state != final:
            next_instructions = self.program[self.state, current_value]
            self.state = next_instructions[0]
            tape_list[tape_pos] = next_instructions[1]
            if next_instructions[2] != '*':
                tape_pos = tape_pos + (1 if next_instructions[2] == 'RIGHT' else -1)
            current_value = tape_list[tape_pos]
            tape = ''.join(tape_list)
            printer = ' ' * tape_pos
            print("STEP: " + str(count) + " STATE: " + next_instructions[0])
            print("POS:  "+printer + '*')
            print("TAPE: "+tape)
            count += 1
            if self.state == reject:
                print("HALT: REJECTED")
            if self.state == final:
                print("HALT: ACCEPTED")

