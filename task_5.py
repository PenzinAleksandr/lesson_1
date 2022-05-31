debit = int(input("Введите выручку фирмы (сумму): "))
credit = int(input("Введите издержки фирмы (сумму): "))


if debit > credit:
    print(f"Выручка больше издержек. Общая рентабельность составляет "
          f"{((debit - credit) / debit):.2f}")  # запутался с рентабельностью, кажется неправильная формула
    employee = int(input("Введите численность сотрудников: "))
    print(f"Прибыль на каждого сотрудника составляет {(debit-credit) / employee}")
elif credit > debit:
    print(f"Издержки больше выручки на {credit - debit}")
else:
    print(f"Выручка равна издержкам")

