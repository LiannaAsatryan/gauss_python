from gauss_functions import *

def main():
    m = read_input()
    golden_list = read_golden()
    output_list = gauss(m)
    write_in_file(output_list)

main()


