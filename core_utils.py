from tabulate import tabulate

class CoreUtils:
    @staticmethod
    def print_table(table_data):
        print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))
