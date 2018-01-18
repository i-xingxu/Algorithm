#coding=utf-8

def maopao_sort(lists):
    '''
    冒泡排序

    它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。

    '''
    try:
        for i in range(0,len(lists)):
            for j in range(i,len(lists)-1):
                if lists[i]>lists[j+1]:
                    lists[i],lists[j+1]=lists[j+1],lists[i]
        return lists
    except Exception as e:
        print(e)


num=[3,5,6,7,2,8,7,10,8,1.100,99,3,4,2222]
a=maopao_sort(num)
print(a)