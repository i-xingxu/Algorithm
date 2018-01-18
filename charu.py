#coding=utf-8

'''
从第一个元素开始，该元素可以认为已经被排序
取出下一个元素，在已经排序的元素序列中从后向前扫描
如果该元素（已排序）大于新元素，将该元素移到下一位置
重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
将新元素插入到该位置后
重复步骤2~5
'''

def charu_sort(lists):
    try:
        count=len(lists)
        if count==1:return lists
        for i in range(1,count):
            for j in range(i,0,-1):
                if lists[j-1]>lists[j]:
                    lists[j-1],lists[j]=lists[j],lists[j-1]
                else:
                    break
        return lists
    except Exception as e:
        print(e)

num=[3,5,6,7,2,8,7,10,8,1,100,99,3,4,2222]
l=charu_sort(num)
print(l)