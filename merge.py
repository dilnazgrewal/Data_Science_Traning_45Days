import nbformat

nb1 = nbformat.read("control_flow_statements (1).ipynb", as_version=4)
nb2 = nbformat.read("python_operators (1).ipynb", as_version=4)

merged = nb1
merged.cells.extend(nb2.cells)

nbformat.write(merged, "merged.ipynb")