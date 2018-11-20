def change_base(n,k):
    ret = []
    while n:
        ret.append(n%k)
        n //= k
    return ret[::-1]

def system(n):
    for i in range(2,n-1):
        tmp = change_base(n,i)
        if tmp == tmp[::-1]:
            return 'NO'
    return 'YES'
q = int(input())
for j in range(q):
    n=int(input())
    print(system(n))