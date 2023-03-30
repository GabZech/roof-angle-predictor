import pandas as pd
import os

directory = "./ignore/data/"

df = pd.DataFrame()

for filename in os.listdir(directory):
    if filename.startswith("hamburg_data"):
        df_temp = pd.read_csv((directory + filename))
        print("Merging " + directory + filename)
        df = df.append(df_temp, ignore_index=True)

print("Number of duplicates being dropped: " + str(df[df.duplicated()].shape[0]))

df = df.drop_duplicates()

print("Number of rows in final cleaned dataset: " + str(df.shape[0]))


df.to_csv("./ignore/data/hamburg_data_clean.csv", index = False)
