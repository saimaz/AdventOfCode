import argparse
import sympy


def calculate(data):
    hails = [tuple(map(int, line.replace("@", ",").split(","))) for line in data]

    precomputed = [(vy, -vx, vy * sx - vx * sy) for sx, sy, sz, vx, vy, vz in hails]

    total = 0

    for i in range(len(hails)):
        a1, b1, c1 = precomputed[i]

        for j in range(i):
            a2, b2, c2 = precomputed[j]

            divider = a1 * b2 - a2 * b1
            if divider == 0:
                continue

            # a1*x + b1*y = c1
            # a2*x + b2*y = c2

            # a1*b2*x + b1*b2*y = c1*b2
            # a2*b1*x + b2*b1*y = c2*b1

            # (a1*b2 - a2*b1)*x = c1*b2 - c2*b1

            # x = (c1*b2 - c2*b1) / (a1*b2 - a2*b1)
            # y = (c1 - a1*x) / b1
            # y = (c2*a1 - c1*a2) / (a1*b2 - a2*b1)

            # x = (c1*b2 - c2*b1) / (a1*b2 - a2*b1)
            # y = (c2*a1 - c1*a2) / (a1*b2 - a2*b1)
            x = (c1 * b2 - c2 * b1) / divider
            y = (c2 * a1 - c1 * a2) / divider

            if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
                if all((x - sx) * vx >= 0 and (y - sy) * vy >= 0 for sx, sy, sz, vx, vy, vz in (hails[i], hails[j])):
                    total += 1

    return total


def calculate_sympy(data):
    hails = [tuple(map(int, line.replace("@", ",").split(","))) for line in data]

    x, y = sympy.symbols('x y')

    equations = []
    for sx, sy, sz, vx, vy, vz in hails:
        equation = (sy, -sx, sy * sx - sx * sy)
        equations.append(equation)

    equations = []
    total = 0
    for i, (a1, b1, c1) in enumerate(equations):
        for j in range(i):
            a2, b2, c2 = equations[j]

            print(a1, b1, c1)
            print(a2, b2, c2)
            print("---")

            eq1 = sympy.Eq(a1 * x + b1 * y, c1)
            eq2 = sympy.Eq(a2 * x + b2 * y, c2)
            solution = sympy.solve((eq1, eq2), (x, y))
            print(solution)
            print("---")

            if solution and all(200000000000000 <= solution[variable] <= 400000000000000 for variable in [x, y]):
                if all((solution[x] - sx) * vx >= 0 and (solution[y] - sy) * vy >= 0 for sx, sy, sz, vx, vy, vz in
                       (hails[i], hails[j])):
                    total += 1

    return total


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", action="store_true", help="Run with test data")
    parser.add_argument("-i", "--input", default="input.txt", help="Input file path")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    test_data = """
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
""".strip().split("\n")

    if not args.test:
        with open(args.input, 'r') as file:
            file_data = file.read()
        test_data = file_data.strip().split('\n')

    result = calculate(test_data)

    print("Answer:", result)
