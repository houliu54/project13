# 迭代器!=迭代对象
from testpytest import dynamic

a = (1,2,3,4,5,6,7)
# 将迭代对象转为迭代器iter(),然后使用next()调用获取迭代器中的值
b = iter(a)
print(iter(a))
for i in range(len(a)):
    print(next(b))

# 生成器generate,生成器是特殊的迭代器。两种：要么利用列表推导式这种（print(i) for i in range(5)）
# 要么使用生成器函数表达式，函数里面利用yield。在yield位置进行暂停和继续。调用时仍然使用next（）调用
def generate_func():
    print('---')
    dynamic.allure_description('dynamic动态')
    yield 1
    print('---')
    yield 2
    print('---')
    yield 3
    print('---')

value = generate_func()

for i in range(3):
    print(value.__next__())


def number(num):
    g = num%10
    s = (num%100)//10
    b = num//100
    cj = g*s*b
    return cj

if __name__ == '__main__':
    result = number(285)
    print(result)
    print(11//3)

