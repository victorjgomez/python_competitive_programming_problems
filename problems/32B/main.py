
# https://codeforces.com/problemset/problem/32/B
if __name__ == '__main__':
    borze_code = str(input())

    borze_code = borze_code.replace("--", "2")
    borze_code = borze_code.replace("-.", "1")
    borze_code = borze_code.replace(".", "0")

    print(borze_code)

