from matrix import *

#this function receives the matrix as a parameter 
#and performs gauss forward elimination
def gauss_forward(m):
    rows = m.get_rows()
    cols = m.get_cols()
    for j in range(rows - 1):
        if(m.get(j, j) != 0):
            for i in range(j+1, rows):
                d = -(m.get(i, j)) / (m.get(j, j))
                m.mull_add(i, j, d)
        else:
            m.swap_with_nonzero_row(j)

#this function performs gauss backward elimination with the given matrix
#and returns the solutions
def gauss_backward(m):
    rows = m.get_rows()
    cols = m.get_cols()
    solutions = []
    for k in range(m.get_rows()):
        solutions.append(0)
    for i in range(rows - 1, -1, -1):
        sum = 0
        for j in range(i + 1, cols - 1):
            sum += m.get(i, j) * solutions[j]
        p = m.get(i, cols - 1) - sum
        solutions[i] = p / m.get(i, i)
    return solutions

#this function performs gauss elimination with the given matrix
def gauss(m):
    gauss_forward(m)
    if(m.exists_wrong_row() or m.exists_zero_row()):
        return None
    return gauss_backward(m)

#this function reads the matrix from the input file and returns the matrix object
def read_input():
    i_file = open("input.txt", 'r')
    input_list = i_file.read().split()
    m = matrix(int(input_list[0]))
    k = 1
    for i in range(m.get_rows()):
        for j in range(m.get_cols()):
            m.set(i, j, float(input_list[k]))
            k = k + 1
    i_file.close()
    return m

#this function reads data from the golden file
def read_golden():
    g_file = open("golden.txt", 'r')
    golden_list = g_file.read().split()
    g_file.close()
    return golden_list

#this function writes the given list or a message into the output file
def write_in_file(list_name):
    o_file = open("output.txt", 'w')
    if(check_input()):
        if(list_name == None):
            o_file.write("no solution")
        else:
            for item in list_name:
                item = float("{0:.7f}".format(item))
                o_file.write(str(item))
                if(item != list_name[len(list_name)-1]):
                    o_file.write(' ')
    else:
        o_file.write("wrong imput")
    o_file.close()
    
#this function compares two lists and returns true if they are similiar
def cmp_lists(list1, list2):
    if(len(list1) != len(list2)):
        return False
    for i in range(len(list1)):
        if( float("{0:.5f}".format(float(list1[i]))) !=  float("{0:.5f}".format(float(list2[i])))):
            return False
    return True

#this function checks a string is a float number
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

#this function returns true if the input is accurate, and returns false otherwise
def check_input():
    i_file = open("input.txt", 'r')
    input_list = i_file.read().split()
    if(input_list[0].isdigit() == False):
        i_file.close()
        return False
    if(len(input_list) != int(input_list[0]) * (int(input_list[0])+1)+1):
        i_file.close()
        return False
    for i in range(len(input_list)):
        if(isfloat(input_list[i]) == False):
            i_file.close()
            return False
    i_file.close()
    return True

