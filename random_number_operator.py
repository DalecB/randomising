import random

num_list = []
for i in range(10000):
    a = random.randint(1, 10000)
    while a in num_list:
        a = random.randint(1, 10000)
    num_list.append(a)


# print(len(num_list))
# print(num_list)
