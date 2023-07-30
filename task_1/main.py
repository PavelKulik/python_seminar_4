from random import randint


n = int(input("Введите кол-во элементов первого множества: "))
m = int(input("Введите ол-во элементов второго множества: "))

list_n = set([randint(0, 10) for i in range(0, n)])
list_m = set([randint(0, 10) for i in range(0, m)])
print("Первое множества:", *list_n)
print("Второе множества:", *list_m)

list_general = set(list_n & list_m)

print("Общее множества:",*list_general)