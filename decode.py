import sys
import numpy as np

# Note this is only for the 2x2 case

ciphertext = sys.argv[1].lower()
key = sys.argv[2].lower()

"""
returns the inverse of the matrix parameter in mod 26
matrix represents some invertible matrix (square numpy array with a non-zero determinant)
"""
def inv(matrix):
    det = int(np.linalg.det(matrix))
    print(det)
    x = 0
    while ((det * x) % 26 != 1): x += 1

    adj = [[matrix[1][1], -1 * matrix[0][1]], [-1 * matrix[1][0], matrix[0][0]]]
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            adj[i][j] *= x
            adj[i][j] %= 26

    return adj

"""
if n is an int, return corresponding char
if n is a char, return corresponding int
"""
def convert(n):
    if type(n) == int:
        return chr(n + 97)
    elif type(n) == str:
        return ord(n.lower()) - 97

for i in "HELP":
    print(convert(i))

"""
cipher_matrix is a n-component vector (i.e [1, 2, 3, 4, 5])
key is a square matrix (i.e [[1, 2], [3, 4]] where the number of elements
must be a perfect square)
key must also be an invertible matrix (hence have a zero determinant)
"""
def decode(cipher_matrix, key):
    plain_matrix = []
    
    for i in range(0, len(cipher_matrix), len(key)):
        chars = []
        for n in cipher_matrix[i:i + len(key)]:
            chars.append([n])
        
        while (len(chars) < len(key)): chars.append([0])

        print(chars)
        dot = inv(key) @ chars

        for n in dot:
            plain_matrix.append(n)

    return plain_matrix

cipher = np.array([[7, 8], [0, 19]])
key = np.array([[3, 3], [2, 5]])
#print(decode(cipher, key))