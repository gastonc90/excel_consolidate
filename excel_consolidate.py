import glob
import pandas as pd
import numpy as np  

all = []


for f in glob.glob("*.xlsx"):
    df = pd.read_excel(f, header = 1, engine = 'openpyxl')
    all.append(df)

df = pd.concat(all,ignore_index='False')

print(df)

df.to_excel("Finales.xlsx")
