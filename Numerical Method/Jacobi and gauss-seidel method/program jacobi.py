import numpy as np

def jacobi(A, b, x_init, epsilon=10**-3, max_iterations=500):
    D = np.diag(np.diag(A))
    LU = A - D
    x = x_init
    for i in range(max_iterations):
        D_inv = np.diag(1 / np.diag(D))
        x_new = np.dot(D_inv, b - np.dot(LU, x))
        if np.linalg.norm(x_new - x) < epsilon:
            return x_new
        x = x_new
        print(x)
    return x

# problem data
A = np.array([[10, -1, 2, 0]\
              ,[-1, 11, -1, 3]\
              ,[2, -1, 10, -1]\
              ,[0, 3, -1, 8]])
b = np.array([6, 25, -11, 15])

# you can choose any starting vector
x_init = np.zeros(len(b))
x = jacobi(A, b, x_init)

print('\nx:', x)
print('computed b:', np.dot(A, x))
print('real b:', b)