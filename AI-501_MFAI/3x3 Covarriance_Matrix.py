X = [12.1, 13.2, 15.6, 17.2, 18.8, 10.3, 11.7, 16.4]
Y = [48, 59, 32, 18, 41, 32, 31, 30]
Z = [101, 171, 112, 132, 140, 112, 151, 96]

n = 8

total_X = 0
total_Y = 0
total_Z = 0

for i in range(n):
    total_X = total_X + X[i]
    total_Y = total_Y + Y[i]
    total_Z = total_Z + Z[i]

mean_X = total_X / n
mean_Y = total_Y / n
mean_Z = total_Z / n

print("Mean of X =", round(mean_X, 2))
print("Mean of Y =", round(mean_Y, 2))
print("Mean of Z =", round(mean_Z, 2))

Xp = []
Yp = []
Zp = []

for i in range(n):
    Xp.append(X[i] - mean_X)
    Yp.append(Y[i] - mean_Y)
    Zp.append(Z[i] - mean_Z)

print("\nNotation:")
print("X' = X - Mean of X")
print("Y' = Y - Mean of Y")
print("Z' = Z - Mean of Z")

print("\nCovariance Calculation Table\n")

print(f"{'X':>12} {'X\'':>12} {'X\'^2':>12} "
      f"{'Y':>12} {'Y\'':>12} {'Y\'^2':>12} "
      f"{'Z':>12} {'Z\'':>12} {'Z\'^2':>12} "
      f"{'X\'Y\'':>12} {'X\'Z\'':>12} {'Y\'Z\'':>12}")

X2 = 0
Y2 = 0
Z2 = 0

XY = 0
XZ = 0
YZ = 0

for i in range(n):

    x_square = Xp[i] * Xp[i]
    y_square = Yp[i] * Yp[i]
    z_square = Zp[i] * Zp[i]

    xy = Xp[i] * Yp[i]
    xz = Xp[i] * Zp[i]
    yz = Yp[i] * Zp[i]

    X2 = X2 + x_square
    Y2 = Y2 + y_square
    Z2 = Z2 + z_square

    XY = XY + xy
    XZ = XZ + xz
    YZ = YZ + yz

    print(f"{X[i]:12.2f} {Xp[i]:12.2f} {x_square:12.2f} "
          f"{Y[i]:12.2f} {Yp[i]:12.2f} {y_square:12.2f} "
          f"{Z[i]:12.2f} {Zp[i]:12.2f} {z_square:12.2f} "
          f"{xy:12.2f} {xz:12.2f} {yz:12.2f}")

print("\nn - 1 =", n - 1)

cov_xx = X2 / (n - 1)
cov_yy = Y2 / (n - 1)
cov_zz = Z2 / (n - 1)

cov_xy = XY / (n - 1)
cov_xz = XZ / (n - 1)
cov_yz = YZ / (n - 1)

print("\nCovariance Matrix:")

print(f"[ {round(cov_xx, 4):>10} {round(cov_xy, 4):>10} {round(cov_xz, 4):>10} ]")
print(f"[ {round(cov_xy, 4):>10} {round(cov_yy, 4):>10} {round(cov_yz, 4):>10} ]")
print(f"[ {round(cov_xz, 4):>10} {round(cov_yz, 4):>10} {round(cov_zz, 4):>10} ]")