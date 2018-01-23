#coding=utf-8

def multiplcation_table():
    '''
    9*9乘法表
    :return:
    '''

    for i in range(1,10):
        for j in range(1,i+1):
            res=i*j
            print("{0}*{1}={2}".format(j,i,res),end="\t")
        print("\n")



multiplcation_table()