# Строковый тип данных - один из самых часто используемых.
# Обозначается - str. Для присвоения переменной str-объекта,
# нужно записать его справа от переменной после знака равно и
# заключить в кавычки (любые).

# Преобразование в строку.
# Используется функция str():
a = 1
b = 1.0
c = [1, 2, 3]
d = (1, 2, 3)
e = {1, 2, 3}
f = {1: 'one', 2: 'two', 3: 'three'}
for i in (a, b, c, d, e, f):
    try:
        print(f"{i} -> {type(i)} {len(i)} -> {str(i)} -> {type(str(i))} {len(str(i))}")
    except TypeError:
        print(f"{i} -> {type(i)} У объекта нет длины -> {str(i)} -> {type(str(i))} {len(str(i))}")

# Конкатенация строк

a = 'Anna'
b = 'Anutka'
c = 'Annushka'
print(a + b + c)
print(b + c + a)

# От перестановки мест слагаемых сумма меняется





