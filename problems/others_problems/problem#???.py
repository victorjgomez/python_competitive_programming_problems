def receive_matrix(r):
    matrix = []
    for i in range(r):
        mx = [int(x) for x in input().split()]
        matrix.append(mx)

    return matrix


def sum_column_even(matrix, number_rows, selected_col):
    sum = 0
    for i in range(number_rows):
        sum = sum + matrix[i][selected_col]

    if sum % 2 == 0:
        return True

    return False


def sum_row_even(matrix, number_column, selected_row):
    sum = 0
    for i in range(number_column):
        sum = sum + matrix[selected_row][i]

    if sum % 2 == 0:
        return True

    return False


def ajust_matrix(matrix, r, c):
    call = False
    for x in range(c):
        for y in range(r):
            if sum_column_even(matrix, number_rows=r, selected_col=x) == False and \
                    sum_row_even(matrix, number_column=c, selected_row=y) == False or c == 1 \
                    and sum_row_even(matrix, number_column=c, selected_row=y) == False:
                matrix[x][y] = matrix[x][y] + 1
                call = True
    return call


if __name__ == '__main__':
    r, c = [int(x) for x in input().split()]
    matrix = receive_matrix(r)

    call = ajust_matrix(matrix, r, c)
    while(call):
        call = ajust_matrix(matrix, r, c)

    print(matrix)