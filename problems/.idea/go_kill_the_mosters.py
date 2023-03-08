import math


def solution(n, k, list_aa, cost = 0):
    half = math.floor(n / 2)
    take = get_take(half, list_aa)
    suma = get_sum(take)

    if len(list_aa) == 0:
        return cost
    elif half == 0:
        solution(len(list_aa), k, [],  cost + list_aa[0])
    elif suma > k:
        list_aa = list_a[half:]
        solution(len(list_aa), k, list_a,  cost + k)
    else:
        list_aa = list_aa[half:]
        solution(len(list_aa), k, list_aa, cost + suma)

def get_take(amount, my_list):
    acc = []
    cont = 1

    for element in my_list:
        if cont > amount:
            break

        acc.append(element)
        cont += 1

    return acc

def get_sum(my_list):
    sum = 0
    for number in my_list:
        sum += number

    return sum


if __name__ == "__main__":
    input1 = list(map(int, input().rstrip().split()))
    n = input1[0]
    k = input1[1]
    list_a = list(map(int, input().rstrip().split()))

    cost = solution(n, k, list_a)

    print(cost)

