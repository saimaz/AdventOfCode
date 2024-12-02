import argparse
import datetime
import importlib.util
import os


def run_script(year, day, part, is_test):
    day_folder = f"{year}/d{day:02d}"
    script_path = os.path.join(day_folder, f"part{part}.py")
    input_file = os.path.join(day_folder, "input.txt")

    spec = importlib.util.spec_from_file_location("script", script_path)
    script_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(script_module)

    data_loader = getattr(script_module, "get_test_data", lambda: open(input_file).read().strip())
    data = data_loader().strip().split("\n") if is_test else load_input_data(input_file)
    result = script_module.solve(data)
    print("Answer:", result)


def load_input_data(input_file):
    with open(input_file, 'r') as file:
        return file.read().strip().split("\n")


def get_default_args():
    now = datetime.datetime.now()
    return {"year": now.year, "day": now.day}


def parse_arguments():
    defaults = get_default_args()
    parser = argparse.ArgumentParser(description="Run Advent of Code solution script.")
    parser.add_argument("-y", "--year", type=int, default=defaults["year"], help="Year of the challenge")
    parser.add_argument("-d", "--day", type=int, default=defaults["day"], help="Day of the challenge")
    parser.add_argument("-p1", action="store_true", help="Run part 1")
    parser.add_argument("-p2", action="store_true", help="Run part 2")
    parser.add_argument("-t", "--test", action="store_true", help="Use test data")
    return parser.parse_args()


def main():
    args = parse_arguments()
    part = 1 if args.p1 else 2 if args.p2 else 1
    print(f"Executing Day {args.day} Part {part}")
    run_script(args.year, args.day, part, args.test)


if __name__ == "__main__":
    main()
