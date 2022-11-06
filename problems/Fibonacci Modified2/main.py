
def fibonacciModified(t1,t2,n):
    if(n==1):
        return t1

    if(n==2):
        return t2


    return fibonacciModified(t1,t2,n-2) + pow(fibonacciModified(t1,t2,n-1),2)

def main():
     I = input()
     I = I.split()

     print(f'{fibonacciModified(int(I[0]),int(I[1]),int(I[2]))}')


main()