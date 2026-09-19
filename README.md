This will be a first repository to test all features of Git, Github, Anaconda and Python together with Visual Studio code. 
The program itself is a small linear algebra calculator that so far can use basic operations: +, -, *, = to add, subtract, calculate the dot product, or set equal two matrices. Additionally the functions trace(), transpose(), pow(), and invert() are available.

Tested the speed of Matrix.inverse() vs numpy.invert(), vs numpy.linalg.inv():
1. For a 3x3 matrix:
   
   Time for numpy.invert(): 3.090 e-5
   
   Time for numpy.linalg.inv(): 2.108 e-2
   
   Time for M.inverse(): 1.515 e-4
   
2.For a 5x5 matrix:

   Time for numpy.invert(): 3.410 e-5
   
   Time for numpy.linalg.inv(): 2.309 e-2
   
   Time for M.inverse(): 3.267 e-4

Based on the numbers for 3x3 and 5x5 matrices numpy.invert() is the computationally fastest method and numpy.linalg.inv() the slowest. The homemade python function is similarly fast as the numpy.invert() function with a difference of approximally one order of magnitude. It would be interesting to see the speed different methods for larger matrices e.g. 10x10 or 100x100.  
For that a reliable invertable matrix generator would be required.  


No AI was used for this project.
