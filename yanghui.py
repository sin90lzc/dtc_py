
# 生成杨辉算法数据

#          1
#         / \
#       / \ / \
#        1   1
#      1   2   1
#     / \ / \ / \
#    1   3   3   1
#   / \ / \ / \ / \
#  1   4   6   4   1
# / \ / \ / \ / \ / \
#1   5   10  10  5   1
def yanghui(level):
    cl=0
    lastList=[]
    result=[]
    while(cl<level):
        lastList=[ x for x in genLevel(lastList)]
        result=[d for d in lastList]
        yield result 
        cl=cl+1

def genLevel(lastList):
    lastList.insert(0,0)
    l=len(lastList)
    for i,v in enumerate(lastList):
        ret=0
        if i==0 or i==l-1:
            ret=1
        else:
            ret=v+lastList[i+1]
        yield ret

for g in yanghui(8):
    print(g)