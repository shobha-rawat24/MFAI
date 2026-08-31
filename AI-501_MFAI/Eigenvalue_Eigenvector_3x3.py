import numpy as np

A = [
    [9.06696429, -10.07678571, -0.72678571],
    [-10.07678571, 159.125, 123.05357143],
    [-0.72678571, 123.05357143, 684.69642857]
]

# Matrix elements
a = A[0][0]
b = A[0][1]
c = A[0][2]
d = A[1][0]
e = A[1][1]
f = A[1][2]
g = A[2][0]
h = A[2][1]
i = A[2][2]

# Characteristic equation:
# |A - lambda I| = 0
# lambda^3 - c2*lambda^2 + c1*lambda - c0 = 0
# c2 = trace(A), c1 = sum of principal 2x2 minors, c0 = determinant(A)

c2 = a + e + i
c1 = (a * e - b * d) + (a * i - c * g) + (e * i - f * h)
c0 = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

print("\nCharacteristic Equation:")
print("|A - lambda I| = 0")
print("\nc2 (Trace) =", round(c2, 6))
print("c1 (Sum of principal 2x2 minors) =", round(c1, 6))
print("c0 (Determinant) =", round(c0, 6))

print("\nCharacteristic Polynomial:")
print("lambda^3 -", round(c2, 6), "lambda^2 +", round(c1, 6), "lambda -", round(c0, 6), "= 0")

# Eigenvalues = roots of characteristic polynomial
coefficients = [1, -c2, c1, -c0]
roots = np.roots(coefficients)
eigenvalues = [root.real for root in roots]
eigenvalues.sort(reverse=True)

print("\nEigenvalues:")
for k in range(3):
    print("lambda" + str(k + 1), "=", round(eigenvalues[k], 6))

# Eigenvectors: (A - lambda I)[x1, x2, x3] = 0

print("\nEigenvectors:")

for lambda_value in eigenvalues:

    print("\nFor lambda =", round(lambda_value, 6))

    A11 = a - lambda_value
    A12 = b
    A13 = c
    A21 = d
    A22 = e - lambda_value
    A23 = f
    A31 = g
    A32 = h
    A33 = i - lambda_value

    # Take x3 = 1
    D = A11 * A22 - A12 * A21

    if abs(D) > 0.000001:
        x3 = 1
        x1 = (-A13 * A22 + A12 * A23) / D
        x2 = (-A11 * A23 + A13 * A21) / D

    else:
        # Take x2 = 1
        D = A11 * A33 - A13 * A31

        if abs(D) > 0.000001:
            x2 = 1
            x1 = (-A12 * A33 + A13 * A32) / D
            x3 = (-A11 * A32 + A12 * A31) / D

        else:
            # Take x1 = 1
            D = A22 * A33 - A23 * A32

            x1 = 1
            x2 = (-A21 * A33 + A23 * A31) / D
            x3 = (-A22 * A31 + A21 * A32) / D

    # Normalize eigenvector
    magnitude = (x1**2 + x2**2 + x3**2) ** 0.5

    x1 = x1 / magnitude
    x2 = x2 / magnitude
    x3 = x3 / magnitude

    print("Eigenvector = [", f"{x1:.6f}", f"{x2:.6f}", f"{x3:.6f}", "]")