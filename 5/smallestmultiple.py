lists = []

for i in range(200000000, 250000000):
    for j in range(1, 21):
        lists.append(i % j)
    print('[' + str(i) + ']' + str(lists))
    if all(x == lists[0] for x in lists):
        print(i)
        break
    lists = []

