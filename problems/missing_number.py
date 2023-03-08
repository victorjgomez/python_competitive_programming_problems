


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().rstrip().split()))

    a.sort()

    i = 1
    while(i<n):
        if(i != a[i-1]):
            print(i)
            break
        i += 1