#coding=utf-8

def erfen_search(lst,start,end,key):


        mid=int((start+end)/2)

        # 为了防止溢出
        # mid=int(start+(end-start)/2)
        if (start>end):
            return -1
        if lst[mid]>key:
            return erfen_search(lst,start,mid-1,key)
        if lst[mid]<key:
            return erfen_search(lst,mid+1,end,key)
        return mid


numbers=[1,2,2,2,2,3,4,5,6,7,8,8,8,9,9,10]
# numbers=range(1,100)

res=erfen_search(numbers,0,len(numbers),2)
print(res)

