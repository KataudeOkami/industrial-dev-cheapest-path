from solution import find_cheapest_path_cost



def main():
    test_triangles = [
        [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]],
        [[-1], [2, 3], [1, -1, -3], [4, 2, 1, 3]],
    ]
    for test_triangle in test_triangles:
        test_find_cheapest_path_cost(test_triangle)


def test_find_cheapest_path_cost(test_triangle):
    print("Исходная пирамида стоимостей:", *test_triangle, sep="\n", end="\n\n")
    costs_triangle, min_cost = find_cheapest_path_cost(test_triangle)
    print("Пирамида конечных стоимостей:", *costs_triangle, sep="\n", end="\n\n")
    print(f"Минимальная стоимость пути от вершины до основания: {min_cost}")
    print("\n")



if __name__ == "__main__":
    main()

