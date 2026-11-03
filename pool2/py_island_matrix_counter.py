def island_matrix_counter(matrix: list[list[str]]) -> int:
    seen = set()
    count = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] != "1" or (r, c) in seen:
                continue
            count += 1
            stack = [(r, c)]
            while stack:
                i, j = stack.pop()
                if (i, j) in seen or not (0 <= i < len(matrix) and 0 <= j < len(matrix[i])):
                    continue
                if matrix[i][j] == "1":
                    seen.add((i, j))
                    stack += [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    return count


if __name__ == "__main__":
    print(island_matrix_counter([["1","0","1"], ["0","1","0"], ["1","0","1"]]))