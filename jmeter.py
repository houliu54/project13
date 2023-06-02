import random


def func(n,a):
    new_name = n+str(random.randrange(1,5))
    new_age = a+str(random.randint(2,5))
    return new_name,new_age


n_name,n_age = func('张三','32')

print(n_name,n_age)