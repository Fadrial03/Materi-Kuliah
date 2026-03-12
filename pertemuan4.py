pendapatan = float(input("Masukkan pendapatan tahunan Anda: "))
pajak = 0

if pendapatan <= 60000000:
    pajak = pendapatan * 0.05
elif pendapatan <= 250000000:
    pajak = pendapatan * 0.15
elif pendapatan <= 500000000:
    pajak = pendapatan * 0.25
else:
    pajak = pendapatan * 0.30

print("Pajak penghasilan yang harus anda bayar adalah", pajak, "rupiah")