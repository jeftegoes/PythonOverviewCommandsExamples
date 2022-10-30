def square(num):
    return num ** 2


print(square(3))


square_lambda = lambda num: num ** 2


print(square_lambda(5))


my_nums = [1, 2, 3, 4, 5, 6]
print(list(map(lambda num:num**2, my_nums)))

print(list(filter(lambda num:num%2 == 0, my_nums)))

names = ["Andy", "Eve", "Sally"]
print(list(map(lambda x:x[::-1], names)))
