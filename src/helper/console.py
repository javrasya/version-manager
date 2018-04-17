from colorama import Fore
from terminaltables import AsciiTable


def print_data(headers, data, title=None):
    print Fore.WHITE
    table_data = [headers]
    for d in data:
        table_data.append(d)
    table = AsciiTable(table_data, title=title)
    print table.table
