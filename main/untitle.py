#coding:utf-8
#一个字符串 s='sdasdadasdasdasdadsasd' ，输入其中一个字母，能返回其第一个和最后一个的index 间距
str='''abbabsbsbdsabdbasbdabdbadsabdab'''

def distance(s,str):
    str=list(str)
    a=[]
    if s in str:
        print('s in string')
        for i in range(len(str)):
            if str[i] in s:
               a.append(i)
        width=(a[-1]-a[0])
        return width
    else:
        print('s is not in str')
        return
#第二种实现方法(返回字符串中某个字母的长度
def maxwidth(s,str):
    #s=input()
    if s in str:
        print('返回的 maxwidth 长度是',str.rindex(s)-str.index(s))
    return str.rindex(s)-str.index(s)

#给一字符串，返回间距最长的字符
def whichdistanceisMaxwidth(str):
    pass



#字符串去重
def DuplicateRemoval(str):
    a=[]
    for i in str:
        if i not in a:
            a.append(i)
    a=''.join(a)
    print(a)
    return a

#字符串去重第二种方法
def DuplicateRemoval2(str):
    a=''
    for i in str:
        if i not in a:
            a=a+i
    print('a=',a)
    return a

#返回长度最大的
def tellmaxwidth(str):
    a={}
    for i in DuplicateRemoval(str):
        a[i]=maxwidth(i,str)
    print(a)
    #print(max(a.values()))

    '''
    for i in a.items():
        if i==max(a.values()):
        '''
    print(a.items())
    type((k for k,v in a.items() if v==max(a.values())))
    return [k for k,v in a.items() if v == max(a.values())]





if __name__=='__main__':
    s = input()
    print(distance(s,str))
    maxwidth(s,str)
    DuplicateRemoval(str)
    DuplicateRemoval2(str)
    print(tellmaxwidth(str))

