def multiply_matrices(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Liczba kolumn w pierwszej macierzy musi być równa liczbie wierszy w drugiej macierzy.")

    rows_a = len(matrix_a)
    columns_a = len(matrix_a[0])
    columns_b = len(matrix_b[0])

    # Tworzenie macierzy wynikowej wypełnionej zerami
    result = [[0 for _ in range(columns_b)] for _ in range(rows_a)]

    # Obliczanie iloczynu macierzy
    for i in range(rows_a):
        for j in range(columns_b):
            for k in range(columns_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result


if __name__ == "__main__":
    matrix_a = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    matrix_b = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]

    try:
        result_matrix = multiply_matrices(matrix_a, matrix_b)
        print("Wynik mnożenia macierzy:")
        for row in result_matrix:
            print(row)
    except ValueError as e:
        print("Błąd:", e)
