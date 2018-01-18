#coding=utf-8

def maopao_sort(numbers):
    '''
    冒泡排序


    '''
    try:
        for i in range(0,len(numbers)):
            for j in range(i,len(numbers)-1):
                if numbers[i]>numbers[j+1]:
                    numbers[i],numbers[j+1]=numbers[j+1],numbers[i]
        return numbers
    except Exception as e:
        print(e)


num=[3,5,6,7,2,8,7,10,8]
a=maopao_sort(num)
print(a)