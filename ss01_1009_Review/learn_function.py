def giai_ptb1(a,b):
    '''
    Đây là phương trình bặc 1 ax + b =0
    :param a: he so a
    :param b: he so b
    :return: nghiem theo a va b
    '''
    if a==0 and b==0:
        return "Vo so nghiem"
    elif a==0 and b!=0:
        return "Vo nghiem"
    else:
        return -b/a

kq1 = giai_ptb1(0,0)
print("0x+0=0 => ",kq1)

def fib(n):
    if n<=2:
        return 1
    return fib(n-1) + fib(n-2)
def pick_fib(n):
    fi=fib(n)
    list_fib = []
    for i in range(1,n+1):
        f_item = fib(i)
        list_fib.append(f_item)
    return fi,list_fib
x,y = pick_fib(6)
print("f6=",x)
print("List 1 to 6 =",y)
