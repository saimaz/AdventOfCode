# Advent of code solutions

My personal attempt to solve Advent of code challenges.

## Requirements
Create `.env` file from `.env.dist` and add a session cookie value from the Advent of Code website. This is required to download the input data for each day.


## Setup

The `setup.py` script is used to create a new folder for each day's challenge and populate it with starter files based on a template.

### Usage
If you want to set up the environment for the current day, just run:

```bash
python3 setup.py
```

To set up the environment for a specific day, run:

```bash
python3 setup.py -y [year] -d [day]
```

## Running Solutions
The run.py script is used to execute the solutions for each part of the day's challenge.

### Usage
To run a solution, use the following command:
    
```bash
python3 run.py -y [year] -d [day] -p1 # For part 1
# or
python3 run.py -y [year] -d [day] -p2 # For part 2
```

This will use `input.txt` as the input file for the solution. If you want to run with the test data, use the `-t` flag:

```bash
python3 run.py -t 
```

Run to calculate final answer for the day:

```bash
python3 run.py 
python3 run.py -p2
```


Challenge's website: https://adventofcode.com/