import sys
import pandas as pd


def run_tpl(code):
    table_name = ""
    columns = []
    rows = []
    data = {}

    for line in code.splitlines():
        commands = line.split()

        if commands and commands[0] == "table":
            table_name = commands[1].replace('"', "")

        if commands and commands[0] == "columns":
            columns = commands[1].split(",")
            for i in range(len(columns)):
                columns[i] = columns[i].replace('"', "")

        if commands and commands[0] == "row":
            row = []
            for thing in commands[1].split(","):
                value = thing.replace('"', "")
                if value.isdigit():
                    row.append(int(value))
                else:
                    row.append(value)
            rows.append(row)

        if commands and commands[0] == "show":
            print(table_name)
            data = {}

            for column in columns:
                data[column] = []

            for row in rows:
                for i, column in enumerate(columns):
                    data[column].append(row[i])

            dataframe = pd.DataFrame(data)
            print(dataframe)


def main():
    if len(sys.argv) < 2:
        print("Using: tpl file.tpl")
        from . import interpreter
        return

    filename = sys.argv[1]

    with open(filename, "r", encoding="utf-8") as f:
        code = f.read()

    run_tpl(code)