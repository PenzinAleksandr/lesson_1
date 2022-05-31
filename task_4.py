num = int(input("Введите целое положительное число: "))
temp_num = 0

while num != 0:
    new_num = num % 10
    if new_num > temp_num:
        temp_num = new_num
    else:
        num = num // 10

print(f"Самая большая цифра в числе {temp_num}")
