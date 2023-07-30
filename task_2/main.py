from random import randint


n = int(input("Введите число кустов с черникой: "))

list_n = [randint(1, 10) for i in range(0, n)]

print(*list_n)
max_el = 0

for i in range(0, len(list_n)):
    if max_el < list_n[i - 2] + list_n[i - 1] + list_n[i]:
        max_el = list_n[i - 2] + list_n[i - 1] + list_n[i]
print(max_el)