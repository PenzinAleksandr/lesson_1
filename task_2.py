users_time = int(input("Введите количество секунд: "))

seconds = users_time % 60
minutes = users_time // 60 % 60
hours = users_time // 3600 % 24  # так как в задании предусмотрен формат вывода чч:мм:сс

print(f"Ваше время {hours:02d}:{minutes:02d}:{seconds:02d}")
