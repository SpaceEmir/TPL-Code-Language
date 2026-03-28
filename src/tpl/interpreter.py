import pandas as pd

class TPSError(Exception):
    pass

table_name = ""
columns = []
rows = []
data = dict()

while True:

    code = input(">>> ")

    for line in code.splitlines():
        commands = line.split()
        if commands and commands[0] == "table":
            table_name = commands[1].replace('"', "")

        if commands and commands[0] == "columns":
            columns = commands[1].split(",")
            for column in range(len(columns)):
                columns[column] = columns[column].replace('"', "")
        
        if commands and commands[0] == "row":
            row = []
            for i, thing in enumerate(commands[1].split(",")):
                row.append(thing.replace('"', ""))
            if len(row) != len(columns):
                raise TPSError("Not given enough data")
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

    if code == "exit":
        break