import glob
import pandas as pd
import numpy as np  

todos = []


for f in glob.glob("*.xlsx"):
    df = pd.read_excel(f, header = 1, engine = 'openpyxl')
    todos.append(df)

df = pd.concat(todos,ignore_index='False')

print(df)

df.to_excel("Finales.xlsx")
