difference = []


def Knapsack(n,c,i,m):

    if (n < 0):
        return 0
    if(i>m-1):
        return 0

    difference.append(n)
    if(n==0):
        return 1


    value = Knapsack(n-c[i],c,i,m)+Knapsack(n,c,i+1,m)

    return value

def main():
    t= int(input())

    while(t>0):
        I = input()
        I = I.split()

        n = int(I[1])
        m = int(I[0])

        I = input()
        I = I.split()

        i=0
        c=[]
        while(i<m):
            c.append(int(I[i]))
            i=i+1

        Knapsack(n, c, 0, m)
        difference.sort()
        print(n-difference[0])
        t=t-1

main()