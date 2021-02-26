import glob
import pandas as pd  


all = []


for f in glob.glob("*.xlsx"):
    df = pd.read_excel(f, header = 1, engine = 'openpyxl')
    all.append(df)

df = pd.concat(all,ignore_index='False')

print(df)

df.to_excel("final_excel.xlsx")
