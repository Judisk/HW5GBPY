N = int(input())
i=result = 1
def Fact(N,i,result):
     if i<N:
        i+=1
        result*=i
     else:
        return result
     return Fact(N,i,result)

def treug(N,i,result):
    if i < N:
        i += 1
        result += i
    else:
        return result
    return treug(N, i, result)

print(f" Факториал числа {N} = {Fact(N,i,result)}")
result=i=1
print(f" Треуголное число {N} = {treug(N,i,result)}")
