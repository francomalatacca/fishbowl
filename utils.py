import re
import time

class Utils:
    @staticmethod
    def is_camel_case(s):
        return bool(re.match(r'^[a-z]+([A-Z][a-z]*)*$', s))

    @staticmethod
    def is_kebab_case(s):
        return bool(re.match(r'^[a-z]+(-[a-z]+)*$', s))

    @staticmethod
    def print_table(table_data):
        col_width = [max(len(str(x)) for x in col) for col in zip(*table_data)]
        for i, row in enumerate(table_data):
            print((" | ".join("{:{}}".format(x, col_width[i]) for i, x in enumerate(row))))
            if i == 0:
                print("-" * (sum(col_width) + 3 * (len(row) - 1)))

    @staticmethod
    def print_hierarchical(d, indent=0):
        for key, value in d.items():
            print("  " * indent + str(key))
            if isinstance(value, dict):
                Utils.print_hierarchical(value, indent + 1)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        Utils.print_hierarchical(item, indent + 1)
                    else:
                        print("  " * (indent + 1) + str(item))
            else:
                print("  " * (indent + 1) + str(value))

    @staticmethod
    def show_loader(message, delay=0.1):
        loader = ["|", "/", "-", "\\"]
        for i in range(10):
            for symbol in loader:
                print(f"\r{message} {symbol}", end="", flush=True)
                time.sleep(delay)
        print("\r" + " " * (len(message) + 2) + "\r", end="", flush=True)
