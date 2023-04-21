
result =0
ia=ib=0
def summa (a,b,ia,ib,result):
    if ia<a:
        result+=1
        ia+=1
    elif ib<b:
        result+=1
        ib+=1
    else:
        return result
    return summa(a,b,ia,ib,result)

print(summa(6,1,ia,ib,result))
