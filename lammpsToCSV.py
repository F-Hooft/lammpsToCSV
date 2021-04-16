import numpy as np
import pandas as pd
from os.path import splitext, isfile
from sys import exit
import click

@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('-o', '--output', "dest", type=click.Path(exists=False), help='Output filename/path.')
def convert(filename, dest):
    if dest is not None:
        output = dest
    else:
        output = splitext(filename)[0] + ".csv"

    if isfile(output):
        print("Output file already exists: {}".format(output))
        exit(1)

    with open(filename, "r") as fp:
        lines = fp.readlines()

    found = False
    data = []
    for line in lines:    
        if not found:
            if "Setting up run" in line:
                found = True
                continue
        if found:
            if "Memory" in line:
                continue
            elif "Step" in line:
                columns = [x for x in line.split(" ") if x != "\n"]
            elif "Loop" in line:
                break
            else:
                k = [float(x) for x in line.split(" ") if x != '' and x != '\n']
                data.append(k)
    df = pd.DataFrame(data, columns=columns)

    df.to_csv(output)

if __name__ == '__main__':
    convert()
