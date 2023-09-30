fnum1 = 1

fnum2 = 1

n = input (" Введіть номер числа Фібоначчі: ")

n = int(n)

i = 0

while i< n-2:

	fnumSum = fnum1 + fnum2

	fnum1 = fnum2

	fum2 = fnumSum

	i = i+1

print("Число Фібоначчі відповідно вашого номеру: ", fnum2)