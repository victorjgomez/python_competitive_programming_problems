
memory_n = {}


def changeWays(n,c,i,m):
    if(n==0):
        return 1
    elif(n<0):
        return 0
    elif(i>m-1):
        return 0
    elif(n in memory_n):
            return memory_n[n]

    value = changeWays(n-c[i],c,i,m)+changeWays(n,c,i+1,m)
    memory_n[n]=value

    print(f'n({n}):{value}')

    return value

def main():
    I = input()
    I = I.split()

    n = int(I[0])
    m = int(I[1])

    I = input()
    I = I.split()

    i=0
    c=[]
    while(i<m):
        c.append(int(I[i]))
        i=i+1

    print(changeWays(n, c, 0, m))

main()