import argparse


class AdventSolver:
    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser(description="Advent of Code Solver")
        parser.add_argument("-t", "--test", action="store_true", help="Run with the test data")
        parser.add_argument("-i", "--input", default="input.txt", help="Input file path")
        return parser.parse_args()

    @staticmethod
    def load_input_data(input_file):
        with open(input_file, 'r') as file:
            return file.read().strip().split("\n")

    def run(self):
        args = self.parse_arguments()
        data = self.get_test_data() if args.test else self.load_input_data(args.input)
        result = self.solve(data)
        print("Answer:", result)

    def solve(self, data):
        raise NotImplementedError("not implemented")

    def get_test_data(self):
        raise NotImplementedError("not implemented")

    @classmethod
    def execute(cls):
        solver = cls()
        solver.run()
