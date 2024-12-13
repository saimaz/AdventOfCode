from typing import List, Tuple
import re


def parse_data(data: List[str]):
    moves = []
    data = [line for line in data if line.strip()]  # Remove empty lines

    a_reg = re.compile(r"Button A: X\+(\d+), Y\+(\d+)")
    b_reg = re.compile(r"Button B: X\+(\d+), Y\+(\d+)")
    prize_reg = re.compile(r"Prize: X=(\d+), Y=(\d+)")

    for i in range(len(data) - 2):
        a = a_reg.match(data[i])
        b = b_reg.match(data[i + 1])
        p = prize_reg.match(data[i + 2])

        if a and b and p:
            button_a = tuple(map(int, a.groups()))
            button_b = tuple(map(int, b.groups()))
            prize = tuple(map(int, p.groups()))
            moves.append((button_a, button_b, prize))
    return moves


def solve(data: List[str]):
    data = [line.strip() for line in data if line.strip()]
    moves = parse_data(data)
    tokens = 0

    for button_a, button_b, prize in moves:
        ax, ay = button_a
        bx, by = button_b
        px, py = prize

        px += 10000000000000
        py += 10000000000000

        # a * ax + b * bx = px
        # a * ay + b * by = py
        # tokens = a * 3 + b

        # b = (px - a * ax) / bx

        # a * ay + ((px - a * ax) / bx) * by = py

        # a = (py - (by * px / bx)) / (ay - (by * ax / bx))
        # b = (px - a * ax) / bx

        b = (px * ay - py * ax) / (bx * ay - by * ax)
        a = (px - bx * b) / ax

        a, b = int(round(a)), int(round(b))
        if ax * a + bx * b == px and ay * a + by * b == py:
            tokens += a * 3 + b

    return tokens


def get_test_data():
    return """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""
