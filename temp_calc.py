from Phasors import Zee

# Define impedances
V_source = Zee.from_polar(45, 30)
V1 = V_source # Node 1 is the positive pole of the generator

L1_imp = Zee(0, 4) # Between Node 1 and Node 2
C1_imp = Zee(0, -3) # Between Node 1 and Node 3
R_L_series = Zee(8, 0) + Zee(0, 5) # Between Node 2 and Node 3
R_C_series = Zee(5, 0) + Zee(0, -2) # Between Node 2 and Node 0
R2 = Zee(10, 0) # Between Node 3 and Node 0

# Define Admittances
Y_L1 = Zee(1,0) / L1_imp
Y_C1 = Zee(1,0) / C1_imp
Y_R_L_series = Zee(1,0) / R_L_series
Y_R_C_series = Zee(1,0) / R_C_series
Y_R2 = Zee(1,0) / R2

# Coefficients matrix A for [V2, V3]
A11 = Y_L1 + Y_R_L_series + Y_R_C_series
A12 = -Y_R_L_series
A21 = -Y_R_L_series
A22 = Y_C1 + Y_R_L_series + Y_R2

# Right-hand side vector B
B1 = V1 * Y_L1
B2 = V1 * Y_C1

# Solve using Cramer's rule for 2x2 system
# Determinant of A
detA = A11 * A22 - A12 * A21

# Solve for V2
detA_V2 = B1 * A22 - B2 * A12
V2 = detA_V2 / detA

# Solve for V3
detA_V3 = A11 * B2 - A21 * B1
V3 = detA_V3 / detA

print(f"V1: {V1}")
print(f"V2: {V2}")
print(f"V3: {V3}")

# Calculate total current from source
# Current leaving Node 1 (total current from generator)
I_total_from_source = (V1 - V2) * Y_L1 + (V1 - V3) * Y_C1

print(f"Total Current from Source: {I_total_from_source}")