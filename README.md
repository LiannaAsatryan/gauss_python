#What this project does
 This project solves the given system of linear equations using Gauss-elimination method

#files
 in this directory there are following files
* input.txt __ it is the file where our matrix example is written like this
	        size
		________
               |       |
               |matrix |
               |_______|

* golden.txt __ it is the file where our correct answer is located
* matrix.py __ here is my matrix class
* gauss_functions.py __ this file contains the functions which solve our main problem (gauss_ forward, gauss_backward, gauss and other related functions) 
* gauss_test.py __ this file  contains the operation of the testing 
* main.py __ this file solves the main problem(without testing)
 the files that will be generated are 
*output.txt__here result-values are written
*result.txt__here test results are written(test passed or not)
*__pycache__(this directory is generated because I import the functions from a file into another)



#description
My project solves the system of linear equations using matrixes
If the system doesn't have solution or the system is linearly dependent the answer is "no solution"
If a letter is typed in place of number, or a wrong size is typed the answer is "wrong imput"
And finally, when our system has solution the answer is written like this   "sol1 sol2 sol3 ... soln"
NOTE: in my output file the solutions are written in 7 precision, in the golden file, 5 precision



#to run the main program type in command line
 python3 main.py
to clean the generated files type 
 rm output.txt
 rm -r __pycache__


#to run the test type in command line
 python3 gauss_test.py
to clean the generated files type 
 rm output.txt result.txt
 rm -r __pycache__
