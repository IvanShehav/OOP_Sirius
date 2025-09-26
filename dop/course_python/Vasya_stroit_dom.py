a, b, d = map(int, input().split())
# a - школа, b - компьютерный клуб
# d - расстояние между киосками

# Расстояние между школой и клубом
dist = abs(a - b)

# Если расстояние четное, то дом можно построить на середине
if dist % 2 == 0:
    house = (a + b) // 2
    print(house, abs(house % d))
else:
    # Если расстояние нечетное, ищем ближайшую точку с минимальной суммой расстояний
    house1 = (a + b) // 2  # Ближайшая точка слева
    house2 = house1 + 1    # Ближайшая точка справа

    # Считаем расстояния до ближайших киосков для обеих точек
    dist1 = min(abs(house1 % d), abs(d - (house1 % d)))
    dist2 = min(abs(house2 % d), abs(d - (house2 % d)))

    # Выбираем оптимальную точку
    if dist1 < dist2:
        print(house1, dist1)
    elif dist2 < dist1:
        print(house2, dist2)
    else:
        # Если оба варианта равны, выбираем точку ближе к киоскам
        if house1 < house2:
            print(house1, dist1)
        else:
            print(house2, dist2)
