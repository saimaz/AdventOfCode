import argparse
import datetime
import urllib.request
import os

from environs import Env
from colorama import Fore, Style


def setup(year: int, day: int) -> None:
    day_folder = f"d{day:02d}"
    directory_path = f"./{year}/{day_folder}"
    os.makedirs(directory_path, exist_ok=True)

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {"Cookie": f"session={env.str('AOC_SESSION_KEY')}"}
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    data = response.read().decode("utf-8")
    input_file_path = f"./{directory_path}/input.txt"
    if not os.path.exists(input_file_path):
        with open(input_file_path, "w") as file:
            file.write(data)

    with open("template.py", "r") as template_file:
        template_content = template_file.read()

    for part in ["part1.py", "part2.py"]:
        file_path = f"{directory_path}/{part}"
        if not os.path.exists(file_path):
            with open(file_path, "w") as part_file:
                part_file.write(template_content)


if __name__ == "__main__":
    env = Env()
    env.read_env()

    parser = argparse.ArgumentParser(description="Download Advent of Code input for a specific day.")
    parser.add_argument("-y", "--year", type=int, default=datetime.datetime.now().year, help="Year of the Advent of code challenge")
    parser.add_argument("-d", "--day", type=int, default=datetime.datetime.now().day, help="Day of the Advent of code challenge")
    args = parser.parse_args()

    current_year = args.year
    current_day = args.day

    setup(current_year, current_day)

    line_width = 70
    star_line = f"{Fore.GREEN}{'*' * line_width}"

    print(star_line)
    print(f"{Fore.GREEN}🎄 Advent of Code {current_year} - Day {current_day} {Style.RESET_ALL} 🧝".center(line_width))
    print(star_line)
    print(f"{Fore.RED}🔍 OPEN {Style.BRIGHT}{Fore.YELLOW}https://adventofcode.com/{current_year}/day/{current_day}{Style.RESET_ALL} for challenge {Style.RESET_ALL}")
    print(star_line)
