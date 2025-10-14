from copy import deepcopy



def find_cheapest_path_cost(triangle):
    N = len(triangle)
    # Чтобы не изменять triangle, лучше сделать
    # глубокую копию и работать уже ней.
    min_costs = deepcopy(triangle)
    # Делаем обход левой и правой вершин
    for i in range(1, N):
        min_costs[i][0] += min_costs[i - 1][0]
        min_costs[i][-1] += min_costs[i - 1][-1]
    # А затем обход всех "внутренних" ячеек
    for i in range(2, N):
        current_row = min_costs[i]
        prev_row = min_costs[i - 1]
        for j in range(1, len(current_row) - 1):
            current_row[j] += min(prev_row[j - 1], prev_row[j])
    return min_costs, min(min_costs[-1])



if __name__ == "__main__":
    print("Модуль, содержащий функцию find_cheapest_path_cost")

