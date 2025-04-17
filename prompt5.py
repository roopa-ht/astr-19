#Write a Python program that writes out a table of the function sin(x) vs. x, where x is tabulated between 0 and 2pi with a thousand entries. 
#Follow the basic Python program structure, including a main program function.

import numpy as np #import numpy to create arrays
from tabulate import tabulate #python built-in package to make tables
from astropy.table import Table #import the class Table from astropy

x = np.linspace(0, 2 * np.pi, 1000)
sin_x = np.sin(x)

table_content = [(y, z) for y, z in zip(x,sin_x)]

table_title = ["x", "sin(x)"]
function_table = tabulate(table_content, tablefmt = "grid", headers = table_title, floatfmt = ".3f")


def main():
	print(function_table)


if __name__ == "__main__":
	main()