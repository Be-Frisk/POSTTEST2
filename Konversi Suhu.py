# Konversi Suhu

print("Program Konversi Suhu dari Celcius ke Fahrenheit,Kelvin, dan Reamur")
Suhu_Celcius = float(input("Masukkan suhu Celcius yang ingin diubah ke Fahrenheit,Kelvin, dan Reamur :"))
Suhu_Fahrenheit = 9./5 * Suhu_Celcius + 32
Suhu_Kelvin = 273 + Suhu_Celcius
Suhu_Reamur = 4/5 * Suhu_Celcius
print("Suhu Celcius adalah : %f" %(Suhu_Celcius), "C")
print("Suhu Fahrenheit adalah : %f" %(Suhu_Fahrenheit), "F")
print("Suhu Kelvin adalah : %f" %(Suhu_Kelvin), "K")
print("Suhu Reamur adalah : %f" %(Suhu_Reamur), "R")
