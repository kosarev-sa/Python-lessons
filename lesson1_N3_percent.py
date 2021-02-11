percent = (int(input("Введите проценты от 1 до 20: ")))
if percent == 1:
    end = ""
elif 1 < percent < 5:
    end = "а"
elif 4 < percent < 21:
    end = "ов"
print(f"Вы ввели {percent} процент{end}")

print("Проверка кода:")
for percent in range(1, 21):
    if percent == 1:
        end = ""
    elif 1 < percent < 5:
        end = "а"
    elif 4 < percent < 21:
        end = "ов"
    print(f"Вы ввели {percent} процент{end}")