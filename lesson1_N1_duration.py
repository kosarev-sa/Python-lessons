duration = (int(input("Введите секунды: ")))
s = duration
m = int(s / 60)
h = int(m / 60)
d = int(h / 24)

if s < 60:
    print(f"{s} сек")

elif s >= 60 and m < 60:
    print(f"{m} мин {s % 60} сек")

elif m >= 60 and h < 24 :
    print(f"{h} час {m % 60} мин {s % 60} сек")

else:
    print(f"{d} дн {h % 24} час {m % 60} мин {s % 60} сек")

print("Проверка кода:")
true_time = [59, 61, 3661, 90061]

for time in true_time:
    s = (int(time))
    m = int(s / 60)
    h = int(m / 60)
    d = int(h / 24)

    if s < 60:
        print(f"{s} сек")

    elif s >= 60 and m < 60:
        print (f"{m} мин {s % 60} сек")

    elif m >= 60 and h < 24:
        print (f"{h} час {m % 60} мин {s % 60} сек")

    else:
        print(f"{d} дн {h % 24} час {m % 60} мин {s % 60} сек")
