def kilkist_dilnikiv(n):
    lichilnik = 0
    for i in range(1, n + 1):
        if n % i == 0:
            lichilnik = lichilnik + 1
    return lichilnik

def suma_cyfr_masyvu(spysok):
    zahalna_suma = 0
    for chyslo in spysok:
        
        for symvol in str(chyslo):
            zahalna_suma = zahalna_suma + int(symvol)
    return zahalna_suma

a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))
k = int(input("Введіть кількість дільників k: "))

masyv = []

for n in range(a, b + 1):
    
    rezultat = kilkist_dilnikiv(n)
    
    if rezultat == k:
        masyv.append(n)

print("Знайдені числа:", masyv)

finalna_suma = suma_cyfr_masyvu(masyv)
print("Сума всіх цифр цих чисел:", finalna_suma)