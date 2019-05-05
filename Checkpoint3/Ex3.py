list = [1, 2, 1, 5, 9, 6, 10, 1, 3, 50, 5]
print(list)
for i in range(len(list) - 1):
    for j in range(len(list) - 1):
        if (list[j] > list[j + 1]):
            a = list[j]
            list[j] = list[j + 1]
            list[j + 1] = a

print(list)
