first_result = float(input("Введите результат первого дня (км): "))
final_result = float(input("Введите требуемый результат (км): "))
day = 1
while first_result < final_result:
    result = first_result / 100 * 10
    first_result += result
    day += 1
print(f"Результат будет достигнут на {day}-й день, и составит {first_result:.2f} км")
