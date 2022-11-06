# https://codeforces.com/problemset/problem/4/C
database = {}


def solution(request: str):
    if database.get(request) is None:
        database[request] = 1
        return "OK"
    else:
        database[request] += 1
        return f"{request}{database[request]-1}"


if __name__ == "__main__":
    n = int(input())

    while n != 0:
        request = input()
        print(solution(request))
        n -= 1
