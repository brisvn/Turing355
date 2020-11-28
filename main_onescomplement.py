"""This is the module to run the ONESCOMPLEMENT turing machine program"""
import getopt
import sys
from turingmachine import TM


def main(argv):
    """This is the main function to run the ONESCOMPLEMENT turing machine program"""
    inputfile = ''
    try:
        opts, arg = getopt.getopt(argv, "hi:o:", ["ifile="])
    except getopt.GetoptError:
        print('usage: main_onescomplement.py -i <inputfile>')

        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main_onescomplement.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg

    program = open("tm_ONESCOMPLEMENT.txt").read()
    ifile = open(inputfile).read()
    turing_machine = TM()
    turing_machine.read(program)
    for line in ifile.splitlines():
        tape = line
        print(line)
        tape_pos = 1
        start = "START"
        end = "FINAL"
        reject = "FINALREJECT"
        turing_machine.execute(tape, tape_pos, start, end, reject)


if __name__ == "__main__":
    main(sys.argv[1:])

