
A  = [
    [9.06696429, -10.07678571, -0.72678571],
    [-10.07678571, 159.125, 123.05357143],
    [-0.72678571, 123.05357143, 684.69642857]
]


print("Covariance Matrix:")

for row in A:
    print("[", end="")
    for value in row:
        print(f"{value:12.4f}", end="")
    print(" ]")


a = A[0][0]
b = A[0][1]
c = A[0][2]

d = A[1][0]
e = A[1][1]
f = A[1][2]

g = A[2][0]
h = A[2][1]
i = A[2][2]


det_A = (
    a * (e * i - f * h)
    - b * (d * i - f * g)
    + c * (d * h - e * g)
)

print("\nDeterminant =", round(det_A, 4))


C11 = +(e * i - f * h)
C12 = -(d * i - f * g)
C13 = +(d * h - e * g)

C21 = -(b * i - c * h)
C22 = +(a * i - c * g)
C23 = -(a * h - b * g)

C31 = +(b * f - c * e)
C32 = -(a * f - c * d)
C33 = +(a * e - b * d)


C = [
    [C11, C12, C13],
    [C21, C22, C23],
    [C31, C32, C33]
]

print("\nCofactor Matrix:")

for row in C:
    print("[", end="")
    for value in row:
        print(f"{value:12.4f}", end="")
    print(" ]")


adj_A = [
    [C11, C21, C31],
    [C12, C22, C32],
    [C13, C23, C33]
]

print("\nAdjoint Matrix:")

for row in adj_A:
    print("[", end="")
    for value in row:
        print(f"{value:12.4f}", end="")
    print(" ]")


if det_A == 0:
    print("\nInverse does not exist.")
else:
    inverse_A = []

    for row in adj_A:
        new_row = []

        for value in row:
            new_row.append(value / det_A)

        inverse_A.append(new_row)

    print("\nInverse of Covariance Matrix:")

    for row in inverse_A:
        print("[", end="")
        for value in row:
            print(f"{value:12.6f}", end="")
        print(" ]")
