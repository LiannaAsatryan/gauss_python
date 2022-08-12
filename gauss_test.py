from gauss_functions import *

def test():
    m = read_input()
    golden_list = read_golden()
    r_file = open("result.txt", 'w')
    output_list = gauss(m)
    write_in_file(output_list)
    if(cmp_lists(output_list, golden_list)):
        r_file.write("test passed")
    else:
        r_file.write("test not passed")
    r_file.close()

test()



    



    

