DIRECTIONS = [(1, 0, "H"), (-1, 0, "H-"), (0, 1, "V"), (0, -1, "V-"), (1, 1, "D1"), (-1, -1, "D1-"), (-1, 1, "D2"), (1, -1, "D2-")]

def prism_detector(grid: list[str], pattern: str):
    if not pattern:
        return []
    result = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            for dx, dy, code in DIRECTIONS:
                word = ""
                for i in range(len(pattern)):
                    nx, ny = x + i * dx, y + i * dy
                    if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]):
                        word += grid[ny][nx]
                if word == pattern:
                    result.append((x, y, code))
    return result

if __name__ == "__main__":
    print(prism_detector(["CAT", "A..", "T.."], "CAT"))
    print(prism_detector(["ABC", "DEF", "GHI"], "CBA"))
    print(prism_detector(["ABC", "DEF", "GHI"], "IEA"))
    print(prism_detector(["ABC", "DEF", "GHI"], "CEG"))
    print(prism_detector([], "CAT"))
    print(prism_detector(["ABC"], ""))
