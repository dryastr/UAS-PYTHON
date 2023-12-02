# SOAL NO. 1
# SOAL NO. 1 BAGIAN A
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

strain = np.array([0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50])
stress = np.array([0.000, 0.252, 0.531, 0.840, 1.184, 1.558, 1.975, 2.444, 2.943, 3.500, 4.115])

slope, intercept, r_value, p_value, std_err = linregress(strain, stress)

plt.scatter(strain, stress, label='Pengukuran')
plt.plot(strain, intercept + slope * strain, 'r', label='Regresi Linear')

plt.xlabel('Strain')
plt.ylabel('Stress (MPa)')
plt.legend()
plt.show()

print(f'Persamaan Regresi Linear: σ = {intercept:.4f} + {slope:.4f}Є')
print(f'Koefisien Korelasi (p): {r_value:.4f}')

# SOAL NO. 1 BAGIAN B
print(f'Nilai a: {intercept:.4f}')
print(f'Nilai b: {slope:.4f}')
print(f'Koefisien Korelasi (p): {r_value:.4f}')

# SOAL NO. 1 BAGIAN C (TERTERA PADA GRAFIK)

# ===================================================================================
# SOAL NO. 2
def f(x):
    return 4*x - x**2

def simpson_rule(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    result = h/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return result

a = 0
b = 1
n = 2

integral_result = simpson_rule(a, b, n)
true_value = -1.3333  # Nilai integral sejati

error = abs(integral_result - true_value)
print(f'Hasil Integral: {integral_result:.4f}')
print(f'Kesalahan Perhitungan: {error:.4f}')


# ===================================================================================
# SOAL NO. 3
x_known = [9.0, 9.5]
y_known = [2.1972, 2.2513]

x_interp = 9.2

# Menggunakan rumus interpolasi linier
y_interp = y_known[0] + (x_interp - x_known[0]) * (y_known[1] - y_known[0]) / (x_known[1] - x_known[0])

true_value_ln_9_2 = 2.2192

print(f'Interpolasi ln(9.2): {y_interp:.4f}')
print(f'Nilai Sejati ln(9.2): {true_value_ln_9_2:.4f}')
