import numpy

# Define the original matrix
matrix = numpy.array([[1, 2], [3, 4], [5, 6]])
print(f'\n# Original Matrix:\n {matrix} \n')

# Tranpose (columns become rows and vice-versa)
matrix_transposed = matrix.T
print(f'\n# Transposed Matrix:\n {matrix_transposed} \n')

# Calculate the mean of each column
columns_means = numpy.mean(matrix_transposed, axis=0)
print(f'\n# Columns Means:\n {columns_means} \n')

"""
# center columns by subtracting column means
C = A - M
print(C)
# calculate covariance matrix of centered matrix
V = cov(C.T)
print(V)
# eigendecomposition of covariance matrix
values, vectors = eig(V)
print(vectors)
print(values)
# project data
P = vectors.T.dot(C.T)
print(P.T)
"""