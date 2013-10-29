import numpy as np
import numpy.linalg as la

def plug_into_matrix(mat, x):
    s = 0
    for n in range(len(mat)):
        s += mat[n] * (x**n)
    return s

def find_FITS(seq): # assumes that len(seq) < n, for generating n-degree polynomial
    lin_matrix = np.zeros((len(seq),len(seq)))
    for i in range(len(seq)):
        for j in range(len(seq)):
            lin_matrix[i,j] = i**j
    function = la.solve(lin_matrix, np.array(seq))
    return plug_into_matrix(function, len(seq))
    
def main():
    sequence = [1 - n + (n**2) - (n**3) + (n**4) - (n**5) + 
                (n**6) - (n**7) + (n**8) - (n**9) + (n**10) for n in range(1,12)]
#     sequence = [n**3 for n in range(1,5)]
    print sequence
    s = 0
    for i in range(1,11):
        t = find_FITS(sequence[:i])
        s += t
        print i, t
    print s
    
main()
