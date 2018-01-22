#coding=utf-8

def quick_sort(lists):
    if len(lists)<=1:
        return lists

    less=[]
    more=[]
    # pop()方法 移除最后一个元素
    key=lists.pop()
    for num in lists:
        if num <key:
            less.append(num)
        elif num>=key:
            more.append(num)
    less=quick_sort(less)
    more=quick_sort(more)
    return less+[key]+more

l=[7,10,9,6,11,99,2,4,6,3,66,7885,44]
print(quick_sort(l))

