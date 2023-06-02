import time

# print(time.time())
# print(time.localtime(time.time()))
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

"""
{上海：{'景区'：['k','y'],'美食':['i','u']}}
{北京：{'景区'：['k','y'],'美食':['i','u']}}
"""

def info():
    count = 0
    content = {}
    while True:
        count+=1
        jq = {}
        place = []
        food = []
        city = input("城市：")
        for i in range(2):
            place.append(input("景区："))
            food.append(input("美食："))
        jq['景区'] = place
        jq['美食'] = food
        content[city] = jq
        if count==2:
            break
    return content


print(info())


