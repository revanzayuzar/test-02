# Program Numerik
# _____________________________________________________________

# Dibuat Oleh : M. Revanza Yuzar (Revan)
# Bahasa Pemrograman : Python
# _____________________________________________________________

# Kode Program :

print("-" * 67)
print("# Program Numerik")
print("-" * 67)

print()

# xi dan yi=f(xi)
x0 = float(input("Masukkan Nilai x0 \t: "))
fx0 = float(input("Masukkan Nilai f(x0) \t: "))

print()

x1 = float(input("Masukkan Nilai x1 \t: "))
fx1 = float(input("Masukkan Nilai f(x1) \t: "))

print()

x2 = float(input("Masukkan Nilai x2 \t: "))
fx2 = float(input("Masukkan Nilai f(x2) \t: "))

print()

x3 = float(input("Masukkan Nilai x3 \t: "))
fx3 = float(input("Masukkan Nilai f(x3) \t: "))

print()

x4 = float(input("Masukkan Nilai x4 \t: "))
fx4 = float(input("Masukkan Nilai f(x4) \t: "))

print("\n\n")

# ST-1
fx1x0 = (fx1 - fx0) / (x1 - x0)
fx2x1 = (fx2 - fx1) / (x2 - x1)
fx3x2 = (fx3 - fx2) / (x3 - x2)
fx4x3 = (fx4 - fx3) / (x4 - x3)

# ST-2
fx2x1x0 = (fx2x1 - fx1x0) / (x2 - x0)
fx3x2x1 = (fx3x2 - fx2x1) / (x3 - x1)
fx4x3x2 = (fx4x3 - fx3x2) / (x4 - x2)

# ST-3
fx3x2x1x0 = (fx3x2x1 - fx2x1x0) / (x3 - x0)
fx4x3x2x1 = (fx4x3x2 - fx3x2x1) / (x4 - x1)

# ST-4
fx4x3x2x1x0 = (fx4x3x2x1 - fx3x2x1x0) / (x4 - x0)

# _____________________________________________________________

print(">> Hasil : \n")

print(f"f[x1, x0] = {fx1x0:.4f}")
print(f"f[x2, x1] = {fx2x1:.4f}")
print(f"f[x3, x2] = {fx3x2:.4f}")
print(f"f[x4, x3] = {fx4x3:.4f}")

print()

print(f"f[x2, x1, x0] = {fx2x1x0:.4f}")
print(f"f[x3, x2, x1] = {fx3x2x1:.4f}")
print(f"f[x4, x3, x2] = {fx4x3x2:.4f}")

print()

print(f"f[x3, x2, x1, x0] = {fx3x2x1x0:.4f}")
print(f"f[x4, x3, x2, x1] = {fx4x3x2x1:.4f}")

print()

print(f"f[x4, x3, x2, x1, x0] = {fx4x3x2x1x0:.4f}")

print("\n\n")

print(">> Tabel Hasil : \n")

print("-------------------------------------------------------------------")
print(f"| i |  xi  | yi=f(xi) |   ST-1   |   ST-2   |   ST-3   |   ST-4   |")
print("-------------------------------------------------------------------")

print("| {} | {:>4} | {:>8} | {:>8.4f} | {:>8.4f} | {:>8.4f} | {:>8.4f} |".format("0", x0, fx0, fx1x0, fx2x1x0, fx3x2x1x0, fx4x3x2x1x0))

print("| {} | {:>4} | {:>8} | {:>8.4f} | {:>8.4f} | {:>8.4f} | {:8} |".format("1", x1, fx1, fx2x1, fx3x2x1, fx4x3x2x1, ""))

print("| {} | {:>4} | {:>8} | {:>8.4f} | {:>8.4f} | {:8} | {:8} |".format("2", x2, fx2, fx3x2, fx4x3x2, "", ""))

print("| {} | {:>4} | {:>8} | {:>8.4f} | {:8} | {:8} | {:8} |".format("3", x3, fx3, fx4x3, "", "", ""))

print("| {} | {:>4} | {:>8} | {:8} | {:8} | {:8} | {:8} |".format("4", x4, fx4, "", "", "", ""))

print("-------------------------------------------------------------------")

print("\n\n")

print("Program Selesai ...")
print()
print("Copyright© 2023 @revanzayuzar")
print()

# Copyright© 2023 @revanzayuzar