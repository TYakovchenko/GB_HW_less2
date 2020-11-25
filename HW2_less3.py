#2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input(). +

list_test = []
count = 0
print("Вам необходимо ввести 5 значений")
while (count < 5):
    test = int(input('Введите  значение'))
    count = count +1
    list_test.append(test)
print("введен список: ", list_test, "\nДавайте попробуем поменять местами:")
if len(list_test) % 2 == 0:
     i = 0
     while i < len(list_test):
         el = list_test[i]
         list_test[i] = list_test[i+1]
         list_test[i+1] = el
         i += 2
else:
    i = 0
while i < len(list_test) - 1:
    el = list_test[i]
    list_test[i] = list_test[i + 1]
    list_test[i + 1] = el
    i += 2
print("Непонятная магия:",list_test)
