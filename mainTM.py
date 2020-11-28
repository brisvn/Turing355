from turingmachine import TM

program = open('tm_SHIFT.txt').read()
tm = TM()
tm.read(program)
tape = "b111110Zbbbbbbbbbbbbbb"
tape_pos = 1
start = "START"
end = "FINAL"
reject = "FINALREJECT"
tm.execute(tape, tape_pos, start, end, reject)
