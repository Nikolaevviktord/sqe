def solve_quadratic_equation(a: float, b: float, c: float) -> dict[str, int]:
    if a == 0:
        return {"It is a linear equation": 42}
    d = b * b - 4 * a * c
    if d < 0:
        return {'D': d, "Solutions": 0}
    elif d == 0:
        solution = -1 * (b / (2 * a))
        return {'D': d, "Solutions": 1, 'Solution 1': solution}
    solution1 = (-1 * b - (d ** 0.5)) / (2 * a)
    solution2 = (-1 * b + (d ** 0.5)) / (2 * a)
    return {'D': d, "Solutions": 2, 'Solution 1': solution1, 'Solution 2': solution2}


import sys
a, b, c = map(float, sys.argv[1:4])
for i, j in solve_quadratic_equation(a, b, c).items():
    print(f"{i}: {j}")
