import argparse
import datetime
import subprocess
import sys


def run_script(year, day, part, test):

    day_folder = f"{year}/d{day:02d}"
    script_path = f"./{day_folder}/part{part}.py"
    input_file = f"{day_folder}/input.txt"

    command = [sys.executable, script_path]
    if test:
        command.append("-t")
    else:
        command.extend(["-i", input_file])

    subprocess.run(command, check=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Advent of Code solution script.")
    parser.add_argument("-y", "--year", type=int, default=datetime.datetime.now().year, help="Year of the challenge")
    parser.add_argument("-d", "--day", type=int, default=datetime.datetime.now().day, help="Day of the challenge")
    parser.add_argument("-p1", action="store_true", help="Run part 1 of the challenge")
    parser.add_argument("-p2", action="store_true", help="Run part 2 of the challenge")
    parser.add_argument("-t", "--test", action="store_true", help="Run with test data")

    args = parser.parse_args()

    if args.p1:
        print(f"Executing Day {args.day} Part 1")
        run_script(args.year, args.day, 1, args.test)
    elif args.p2:
        print(f"Executing Day {args.day} Part 2")
        run_script(args.year, args.day, 2, args.test)
    else:
        print(f"Executing Day {args.day} Part 1")
        run_script(args.year, args.day, 1, args.test)
