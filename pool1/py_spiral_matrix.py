
def generate_spiral(n : int) -> list[list[int]]:
    if n <= 0:
        return []
    matrix = [[0] * n for _ in range(n)]
    r, c, dr, dc = 0,0,0,1
    for num in range(1, n * n + 1):
        matrix[r][c] = num
        nr, nc = r + dr, c + dc
        if not (0 <= nr < n and 0 <= nc < n and matrix[nr][nc] == 0):
            dr, dc = dc, -dr
        r, c = r + dr, c + dc
    return matrix

if __name__ == "__main__":
    print(generate_spiral(3))